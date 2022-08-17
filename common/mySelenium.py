# coding=utf-8

from selenium import webdriver
import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import common.logger


class mySelenium:

    def __init__(self):
        # LOG_FORMAT = "[%(asctime)s]-[%(levelname)s] %(message)s"
        # DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
        # logging.basicConfig(filename=r'D:\pycharm\20220412\webuitest\report\my.log',
        #                     level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
        self.log = common.logger.Logger(r"/report\my.log")

    def openBrowser(self, browserType):
        self.driver = None
        if "chrome" == browserType.lower():
            self.driver = webdriver.Chrome()
        elif "ie" == browserType.lower():
            self.driver = webdriver.Ie()
        else:
            logging.error("error browerType")
        self.driver.maximize_window()
        return self.driver

    def quit(self):
        self.driver.quit()

    def get(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(30)  # 隐式等待，页面加载，元素加载


    def findElement_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def findElements_by_xpath(self, xpath, num):
        return self.driver.find_elements(By.XPATH, xpath)[num]

    def elemSendkeys(self, xpath, value):
        self.driver.find_element(By.XPATH, xpath).clear()
        return self.driver.find_element(By.XPATH, xpath).send_keys(value + Keys.RETURN)

    def elemsSendkeys(self, xpath, num, value):
        self.driver.find_element(By.XPATH, xpath).clear()
        return self.driver.find_elements(By.XPATH, xpath)[num].send_keys(value + Keys.RETURN)




if __name__ == "__main__":
    mysele = mySelenium()
    mysele.openBrowser("chrome")
