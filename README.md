# <口袋助理> 自动写日报脚本

自动抓取本地 Git 仓库当天 Commit 信息，组织后通过 Selenium Webdriver 模拟登陆、页面跳转、填写表单并提交到当日日报中。

> 本代码仅供学习研究使用！

### Requirements
- [Selenium](http://www.seleniumhq.org)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- [GitPython](https://github.com/gitpython-developers/GitPython)

### Show

![chrome_demo](https://raw.githubusercontent.com/godblesshugh/KD77AutomationWorkDaily/master/chrome_demo.gif)


### Dev Log

* 使用 ChromeDriver 解决兼容性以及启动速度慢的问题。
* 使用 WebDriverWait 解决 time.sleep() 不准确的问题
* 兼容 Python2 和 Python3
