# <口袋助理> 自动写日报脚本

自动抓取本地 Git 仓库当天 Commit 信息，组织后通过 Selenium Webdriver 模拟登陆、页面跳转、填写表单并提交到当日日报中。

> 本代码仅供学习研究使用！

### Requirements
- [Selenium](http://www.seleniumhq.org)
- [GitPython](https://github.com/gitpython-developers/GitPython)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

### Show

![chrome_demo](https://raw.githubusercontent.com/godblesshugh/KD77AutomationWorkDaily/master/chrome_demo.gif)


### Help

* 使用 ChromeDriver 解决兼容性以及启动速度慢的问题。
* 使用 WebDriverWait 解决 time.sleep() 不准确的问题

> Error: Unable to access jarfile selenium-server-standalone-2.53.0.jar

如果出现这个错误，你需要下载 [Selenium Standalone Server](http://www.seleniumhq.org/download/) 到同一目录，然后修改一下代码中对应文件名

另外可能还需要安装 SafariDriver，Safari 的一个扩展，也在上面同一个地方下载。
