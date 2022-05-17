# Author:Shirley
# Date:2022-05-17
# 百度搜索页面对象
# 基于业务层来获取页面的相关核心元素内容，并实现业务的封装
from webui03.base.base_page import BasePage


class SearchPage(BasePage):
    # 页面url
    url = 'http://www.baidu.com'
    # 页面核心元素
    el_input = ('id', 'kw')
    el_button = ('id', 'su')

    # 搜索业务封装
    def search(self, txt):
        self.open(self.url)
        self.input(*self.el_input, txt=txt)
        self.click(*self.el_button)
