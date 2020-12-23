#-*-coding:utf-8-*-
__author__ = 'tanz'
#打开估价宝09环境
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import os


a=webdriver.Ie()
a.get("http://gjb.fxtchina.com")
a.find_element(By.ID,"txtusername")
a.find_element_by_id("txtusername").clear()
a.find_element_by_id("txtusername").send_keys("tan1@gjb")
a.find_element_by_id("txtpassword").send_keys("654321")
a.find_element_by_id("btnlogin").click()
time.sleep(3)
a.find_element_by_xpath("//ul[@id='quicklinks']/li[2]").click()
time.sleep(3)
a.find_element_by_id("tree_246_203_span").click()
time.sleep(3)
a.switch_to_frame("mytab_203Frame")
#a.find_element_by_id("chk_131178").click()
#a.find_element_by_id("btnCopy").click()
ActionChains(a).move_to_element(a.find_element_by_id("addObject")).perform()
time.sleep(2)
a.find_element_by_xpath("//*[@id='addObject']/ul/li[1]").click()
time.sleep(4)

'''
a=webdriver.Chrome()
a.get("http://gjb.fxtchina.com")
a.find_element_by_id("txtusername").clear()
a.find_element_by_id("txtusername").send_keys("tan1@gjb")
a.find_element_by_id("txtpassword").send_keys("654321")
a.find_element_by_id("btnlogin").click()
time.sleep(5)
a.find_element_by_xpath("//ul[@id='quicklinks']/li[4]").click()
time.sleep(2)
a.find_element_by_id("tree_201_212_span").click()
time.sleep(8)
a.switch_to_frame("mytab_212Frame")
a.find_element_by_id("btnAdd").click()
'''
