# coding=utf-8

import common.base as base
import common.mySelenium as mySelenium
import logging
import pytest



class Test_baidu:

    def setup_class(self):
        logging.info(" --- setup_class --- ")
        self.sele = mySelenium.mySelenium()
        self.sele.openBrowser("chrome")
        self.sele.get("https://blog.csdn.net/qq_41341757/article/details/109194627")
        self.sele.log.info("setup_class1111")



    def teardown_class(self):
        logging.info(" --- teardown_class --- ")
        # self.sele.quit()

    def test_click1(self):
        self.sele.findElement_by_xpath(r"//*[@id='directory']/div/div/div/div/ol/li[6]/a").click()
        logging.info("click1 ")

    def test_click2(self):
        self.sele.findElement_by_xpath(r"//*[@id='directory']/div/div/div/div/ol/li[6]/a").click()
        logging.info("click2 ")







