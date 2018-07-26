#coding=utf-8
from selenium import webdriver
import logging
import time
bro = webdriver.Chrome()
bro.get("http://hao123.com")
# bro.get("http://baidu.com")
# bro.find_element_by_name("wd").send_keys("bigbang")
# bro.find_elements_by_id("su").click()
bro.find_element_by_id("search-input").send_keys("selenium")
# bro.find_element_by_id("button").click()
#
logging.info("start")
bro.find_element_by_class_name("button").click()
# bro.find_element_by_xpath("//div[@class='button-hook']").click()
logging.info("end")
# bro.quit()
# logging.warn("error")
#打印信息
data = bro.find_element_by_id("search-input").text
print(data)
time.sleep(3)
bro.quit()