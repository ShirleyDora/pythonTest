# Author:Shirley
# Date:2022-05-15
# 元素定位方法：
# 八种1.id;id=""唯一
# 2.name;name=""
# 3.link text;定位超链接<a标签的文本>
# 4.partial link text;<a标签里文本模糊查找>不加s进行定位，默认返回第一个；加s,返回下标的选择
# 5.tagname;标签名一般复数用s,及其不推荐使用，很多重复，ul里有很多li,统计商品个数
# 6.classname;class=""不推荐使用
# 7.cssselector;万金油#kw专治IE浏览器下的元素定位疑难杂症右键F12Copy Selector
# form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap>aaa>bbb
# 8.xpath
# xpath相对路径推荐: //*[@id="kw"]或//input[@id="kw"]
# //从html查找，
# input查找标签名，
# []添加筛选条件 and多条件筛选
# @表示属性（Attribute)
# //input[@type="hidden"and @name="ch"]
# //form[@name="f"/input[5]] 通过父元素定位子元素
# //input[@type="hiden"]/.. 通过子元素定位父元素
# full xpath绝对路径不推荐:  /html/body/div[1]/div[1]/div[5]/div/div/form/span[1]
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# el=driver.find_element_by_id('kw')
# print(type(el))
# el=driver.find_element_by_name('wd')
# el=driver.find_element_by_link_text('新闻')
# el.click()
# print(type(el))
# el=driver.find_element_by_partial_link_text('外交部')
# 默认返回一个list
# els=driver.find_elements_by_partial_link_text('百度')
# for el in els:
#     print(el.text)
# els = driver.find_elements_by_tag_name('a')
# for el in els:
#     print(el.text)
# el = driver.find_elements_by_class_name('blue')
driver.find_element(By.ID, 'AAA')
driver.find_element('id', 'aaa')
# By.XPATH=xpath
# 优先使用下面的
driver.find_element('xpath', '//a[contains(text(),"新”)]')
# 切换新网页
handles = driver.window_handles
driver.switch_to.window(handles[1])
print(driver.title)
driver.switch_to.frame(driver.find_element('id', 'ptlogin_iframe'))
