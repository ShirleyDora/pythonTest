# Author:Shirley
# Date:2022-05-15
# 百度的搜索执行
# 从webdriver模块的底层代码应用来了解selenium+webdriver对浏览器进行交互应用
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

# 启动浏览器
# driver = webdriver.Chrome()
wd = WebDriver(executable_path='chromedriver')
# 访问url
# driver.get('http://www.baidu.com')
wd.execute('get',{'url':'http://www.baidu.com'})
# 输入Shirley你好呀20220515
# driver.find_element_by_id('kw').send_keys('Shirley你好呀20220515')
el = wd.execute('findElement',{
    'using':'xpath',
    'value':'//input[@id="kw"}'})['value']
print(type(el))
el._excute('sendKeysToElement',{
    'text':'666Shilrey20220515',
    'value':''
})

# 点击百度一下按钮实现搜索
# driver.find_element_by_id('su').click()
el = wd.execute('findElement',{
    'using':'xpath',
    'value':'//input[@id="su"}'})['value']
print(type(el))
el._excute('clickElement')
# 关闭浏览器释放进程资源
sleep(3)
# driver.quit()
