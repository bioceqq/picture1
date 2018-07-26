# coding:utf-8

import unittest,time

from qq.log import Log

from selenium import webdriver

log = Log()

class Test(unittest.TestCase):
#每个测试用例执行之前的操作
    def setUp(self):

        self.driver = webdriver.Chrome()

        self.driver.get("https://www.baidu.com")

        self.driver.implicitly_wait(30)#智能等待30s

    def test_01(self):

        log.info("-------测试用例开始---------")

        self.driver.find_element_by_id("kw").send_keys("yoyo")

        log.info("输入内容：yoyo")

        self.driver.find_element_by_id("su").click()

        log.info("点击按钮：id = su")

        time.sleep(2)

        t = self.driver.title

        log.info(u"获取title内容：%s"%t)

        self.assertIn(u"百度搜索",t)#断言（u in t）
#每个测试用例执行之后的操作
    def tearDown(self):

        self.driver.quit()

        log.info("-------测试用例结束----------")

if __name__ == "__main__":

    unittest.main()