from selenium import webdriver as web

from appium import webdriver as app
import allure


class Test001:

    def setup_class(self):
        self.web = web.Firefox()
        self.web.get("http://www.baidu.com")

        desired_caps = {
            'platformName': 'Android',  # 平台
            'platformVersion': '5.1',  # 平台所属版本
            'deviceName': '192.168.56.101:5555',  # 设备名字 随便写
            'appPackage': 'com.android.settings',  # app包名
            'appActivity': '.Settings'  # app启动名
        }
        # 声明驱动对象 创建session 打开启动参数中指定的app
        self.app = app.Remote('http://localhost:4723/wd/hub', desired_caps)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("web截图")
    def test_001(self):
        allure.attach(self.web.get_screenshot_as_png(), "web截图", allure.attachment_type.PNG)

    @allure.step("app截图")
    def test_002(self):
        allure.attach(self.app.get_screenshot_as_png(), "web截图", allure.attachment_type.PNG)
