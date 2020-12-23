#-*-coding:utf-8-*-
__author__ = 'tanz'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import unittest
driver = webdriver.Chrome()
#driver.get("http://baidu.com")

'''
print "浏览器高度调整"
driver.set_window_size(800,800) #浏览器高度调整
time.sleep(4)
print "浏览器最大化"
driver.maximize_window()  #浏览器最大化
time.sleep(3)
driver.quit()
'''

'''
first_url = "http://www.baidu.com"
print "now access %s"%(first_url)  # %s表示输出的类型为字符串，%d表示输出的类型为整形数字
driver.get(first_url)  #访问百度首页
second_url = "http://www.news.baidu.com"
print "now access %s"%(second_url)
driver.get(second_url)  #访问新闻页面
time.sleep(3)
driver.back() #返回到百度首页
time.sleep(3)
driver.forward()  #前进到新闻页面
time.sleep(2)
driver.quit()
'''

'''
b.find_element_by_id()  #常见定位方式
b.find_element_by_name()
b.find_element_by_class_name()
b.find_element_by_tag_name()
b.find_element_by_text_link()
b.find_element_by_partial_text_link()
b.find_element_by_xpath()
b.find_element_by_css_selector()

clear() #清除元素内容(常用操作元素方法)
send_keys() #模拟按键输入，输入内容
click()  #单击元素
submit() #提交元素
'''

'''
size=driver.find_element_by_id("kw").size  #获取元素的尺寸
text=driver.find_element_by_id("cp").text  #获取元素的文本
attribute=driver.find_element_by_id("kw").get_attribute("name")  #获得属性值
result=driver.find_element_by_id("kw").is_displayed()  #返回元素结果是否可见，返回值为True或False
print size,text,attribute,result
'''

'''
driver.get("http://gjb.yungujia.com")
right = driver.find_element_by_id("btnlogin")
#ActionChains(driver).context_click(right).perform()  #右击
#ActionChains(driver).double_click(right).perform()  #双击
#ActionChains(driver).drag_and_drop(source,target).perform()  #鼠标拖放
#ActionChains(driver).move_to_element(right).perform()  #鼠标移动到元素上
ActionChains(driver).click_and_hold(right).perform()  #按住鼠标左键
time.sleep(3)
driver.quit()
'''

'''
driver.get("http://gjb.yungujia.com")
driver.find_element_by_id("txtusername").clear()
driver.find_element_by_id("txtusername").send_keys("tan1@gjbp")
driver.find_element_by_id("txtusername").send_keys(Keys.BACK_SPACE)  #删除多输入的一个字符（删除最后的字符“p”）
driver.find_element_by_id("txtpassword").send_keys(Keys.SPACE)  #加入空格键
driver.find_element_by_id("txtpassword").send_keys("a654321")
driver.find_element_by_id("txtusername").send_keys(Keys.CONTROL,"a")  #ctrl+a 全选输入框内容
#driver.find_element_by_id("txtusername").send_keys(Keys.CONTROL,"x")  #ctrl+x 剪切输入框内容
#driver.find_element_by_id("txtusername").send_keys(Keys.CONTROL,"v")  #输入框重新输入内容，搜索（复制）
driver.find_element_by_class_name("login-btn").send_keys(Keys.ENTER)  #通过回车键盘来代替点击操作
time.sleep(4)
driver.quit()

send_keys(Keys.TAB)  制表键  #其他常用键盘操作
send_keys(Keys.ESCAPE)  回退键
send_keys(Keys.CONTROL,"c")  复制
'''

