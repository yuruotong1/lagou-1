from appium import webdriver
from selenium.webdriver.common.by import By


class TestWebview:
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def test_webview(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = self._package
        caps["appActivity"] = self._activity
        caps["noReset"] = True
        # 需要对应版本的 chromedirver ，才能在 webview 中执行 js 代码
        caps["chromedriverExecutable"] = "C:/develop/chromedriver/chromedriver2.20.exe"
        # 初始化driver
        self._driver = webdriver.Remote(
            "http://localhost:4723/wd/hub",
            caps)
        self._driver.implicitly_wait(15)
        # 进入到 webview
        self._driver.find_element(By.XPATH, "//*[@text='交易']").click()
        # 切换上下文到 webview
        webview = self._driver.contexts[-1]
        self._driver.switch_to.context(webview)
        # 执行 js 代码，获取性能数据
        all_time = self._driver.execute_script("return window.performance.timing")
        # 对数据进行二次操作
        response_time = all_time['responseEnd'] - all_time['responseStart']
        print(response_time)
