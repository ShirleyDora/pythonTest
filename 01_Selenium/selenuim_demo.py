# Author:Shirley
# Date:2022-05-15
# 百度的搜索执行
# 导入selenium模块
from time import sleep

from selenium import webdriver

# 启动浏览器
driver = webdriver.Chrome()
# 访问url
driver.get('http://www.baidu.com')
# 输入Shirley你好呀20220515
driver.find_element_by_id('kw').send_keys('Shirley你好呀20220515')
# 点击百度一下按钮实现搜索
driver.find_element_by_id('su').click()
# 关闭浏览器释放进程资源
sleep(3)
driver.quit()
