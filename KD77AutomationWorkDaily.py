import os
import time, datetime
from git import Repo
from selenium import webdriver

# import requests
# import http.cookiejar
# import urllib.parse

# Git 仓库路径
repo_dir = ""

# Git 仓库分支
repo_branch = "master"

# Git 仓库提交人邮箱
author_email = ""

# 口袋助理账号密码
kd77_username = ""
kd77_password = ""

# ---------------------

# 任务开始...
def Work_Report():

    if not repo_dir:
        print("未指定本地 Git 仓库路径.")
        return
    if not author_email:
        print("未指定 Git 提交人邮箱.")
        return

    #
    repo = Repo(repo_dir)

    today = datetime.datetime.today()
    today_commit_messages = []

    for commit in repo.iter_commits(repo_branch):
        if commit.author.email == author_email:
            commit_datetime = datetime.datetime.fromtimestamp(commit.committed_date)
            if commit_datetime.year == today.year and commit_datetime.month == today.month and commit_datetime.day == today.day :
                today_commit_messages.append(commit.message.strip())

    # 输出今天的 Commit
    today_commit_messages_string = ""
    if today_commit_messages:
        for commit_message in today_commit_messages:
            today_commit_messages_string = today_commit_messages_string + ' - ' + commit_message + '\n'
        
        print("\n--- 今天提交的 Commit ---\n")
        print(today_commit_messages_string)
        print("\r")

        return today_commit_messages_string
    else:
        print("今天没有 Commit")
        return

# 提交日报到 <口袋助理>
def Write_Daily(commit_messages):
    print("准备开始写日报...")

    if not kd77_username or not kd77_password:
        print("未指定口袋助理账号密码")
        return

    try:
        # SafariDriver
        os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.53.0.jar"
        browser = webdriver.Safari()
        # browser = Safari()
        browser.get("https://web.kd77.cn")

        print(browser.title)

        # browser.get_screenshot_as_file("/Users/isaced/Desktop/befor.png")

        # username
        browser.execute_script('document.getElementById("ext-comp-1001-username").value="' + kd77_username+ '"')
        browser.execute_script('document.getElementById("ext-comp-1001-pwd").value="' + kd77_password +'"')

        # # login
        login_btn = browser.find_element_by_id('ext-comp-1001-btn')
        login_btn.click()

        # login Error !!!
        # time.sleep(1)
        # lgoin_error = browser.find_element_by_id('ext-comp-1001-tips-msg').text
        # print("----------")
        # print(browser.find_element_by_id('ext-comp-1001-tips-msg'))
        # print("-----")
        # if len(lgoin_error) > 0:
        #     print(lgoin_error)
        #     return

        print(browser.current_url)

        print("wait 5 sec...")
        time.sleep(4)
        print("wait 4 sec...ok")

        print("跳转到我的工作汇报...")
        browser.find_element_by_xpath("//li[@path='0-5']").click() # 工作汇报
        time.sleep(1)
        browser.find_element_by_xpath("//li[@path='0-5-0']").click() # 我的工作汇报
        time.sleep(3)

        print("点开写工作汇报表单...")
        browser.find_element_by_xpath("//button[contains(text(),'写工作汇报')]").click() # 写工作汇报
        time.sleep(1)
        browser.find_element_by_xpath("//span[contains(text(),'写日报')]").click() # 写日报
        time.sleep(1)

        print("写入今日工作总结...")
        browser.find_element_by_xpath("//textarea[@name='今日工作总结']").send_keys(commit_messages)

        print("明日工作计划...")
        browser.find_element_by_xpath("//textarea[@name='明日工作计划']").send_keys("～")

        print("提交工作汇报表单...")
        browser.find_element_by_xpath("//button[contains(text(),'确定')]").click()

        # 发请求还是不行，不知为何
        
        # post 
        # workreport_json = {"wrdate":1459526400000,"reportType":0,"opr":"create","content":None,"forms":[{"content":"1111111","formName":"今日工作总结","required":1},{"content":"222222","formName":"明日工作计划","required":1}],"attrs":[]}

        # headers = {
        #     "Accept":"*/*",
        #     "Accept-Encoding":"gzip, deflate",
        #     "Accept-Language":"zh-CN,zh;q=0.8",
        #     # "Connection":"keep-alive",
        #     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        #     "Host":"web.kd77.cn",
        #     "Referer": "https://web.kd77.cn/m/index.php",
        #     "session-token":"no-token",
        #     "X-Requested-With":"XMLHttpRequest",
        #     "Content-Type":"application/json"
        # }

        # cookies = {}
        # for s in browser.get_cookies():
        #     cookies[s['name']] = s['value']
        # print(cookies)
        # # session = requests.Session()
        # # requests.utils.add_dict_to_cookiejar(session.cookies, cookies)
        # print("begin post...")
        # workreport_request = requests.post('https://web.kd77.cn/server/index.php/mod_workreport', data = workreport_json, headers=headers, cookies=cookies)
        # print("end post...")
        # print(workreport_request.text)
        # print(browser.current_url)
        # print(browser.title)
    finally:
        print("任务完成...")
        browser.quit()

if __name__ == "__main__":
    # 读取今天的 Git commit message
    today_commit_messages_string = Work_Report()

    # 如果有 Commit，那就写到 <口袋助理> 今天的日报里吧
    if today_commit_messages_string:
        Write_Daily(today_commit_messages_string)