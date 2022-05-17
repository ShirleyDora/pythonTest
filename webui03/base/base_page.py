# Author:Shirley
# Date:2022-05-17
# 基类：作为整个框架的底层逻辑处理。
# 类似于关键字驱动的底层逻辑实现
from selenium import webdriver


class BasePage:
    driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 元素定位
    def locate(self, by, value):
        return self.driver.find_element(by, value)

    # 输入
    def input(self, by, value, txt):
        self.locate(by, value).send_keys(txt)

    # 点击
    def click(self, by, value):
        self.locate(by, value).click()
