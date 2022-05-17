# Author:Shirley
# Date:2022-05-17
import unittest
from time import sleep

from ddt import ddt, file_data
from selenium import webdriver

from webui03.page_object.search_page import SearchPage


@ddt
class CaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    # 测试用例
    @file_data('../data/search.yaml')
    def test_01_search(self, txt):
        # driver = webdriver.Chrome()
        # sp = SearchPage(driver)
        sp = SearchPage(self.driver)
        sp.search(txt)
        sleep(3)


    def test_02(self):
        self.driver.get('http://www.jd.com')



if __name__ == '__main__':
    unittest.main()

