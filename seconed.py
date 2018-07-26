#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
import os,time
driver = webdriver.Chrome()
driver.get("http://my.jjwxc.net/login.php?referer=http%3A%2F%2Fmy.jjwxc.net%2Fonebook_vip.php%3Fnovelid%3D3366589%26chapterid%3D23")
time.sleep(3)
driver.maximize_window()# 浏览器全屏显示

driver.find_element_by_name("loginname").clear()
driver.find_element_by_id("loginname").send_keys("18700469957")
#tab 的定位相相于清除了密码框的默认提示信息，等同上面的 clear()
# driver.find_element_by_id("fm-login-id").send_keys(Keys.TAB)
time.sleep(3)
driver.find_element_by_name("loginpassword").send_keys("0917qq")
# driver.find_element_by_id("fm-login-password").send_keys("123456")
#通过定位密码框，enter（回车）来代替登陆按钮
driver.find_element_by_name("loginpassword").send_keys(Keys.ENTER)
'''
# #也可定位登陆按钮，通过 enter（回车）代替 click()
# driver.find_element_by_id("login").send_keys(Keys.ENTER)
# #'''
time.sleep(3)
driver.quit()