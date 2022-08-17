# coding=utf-8

import logging
import time
import common.base
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_html
import os

# @pytest.fixture(scope="function", name='driver', params=[webdriver.Chrome()], ids=['Chrome'])
# def test_open1(driver):
#     driver.find_element(By.XPATH, "//*[@id='s-top-left']/a[1]").click()
#     logging.info("新闻")
#     driver.switch_to.window(driver.window_handles[0])
#     logging.info("切换到第一个窗口")
#     time.sleep(3)
#
#
# def test_open2(driver):
#     driver.find_element(By.XPATH, "//*[@id='s-top-left']/a[3]").click()
#     logging.info("地图")


@pytest.fixture(scope="class")
# @pytest.fixture(scope="function")
def test_00():
    logging.info("test_00")


@pytest.fixture(scope="session")
def test_01():
    logging.info("test_01")


@pytest.fixture(scope="module")
def test_02():
    logging.info("test_02")

class Test_class1:

    @pytest.fixture(scope="function")
    def test_03(self):
        logging.info("test_03")

    def test_04(self, test_00, test_01, test_02, test_03):
        logging.info("test_04")
        logging.info(test_00)

    def test_05(self, test_00, test_01, test_02, test_03):
        logging.info("test_05")
        logging.info(test_00)
def test_000():
    allureDir = common.base.createDir(r"report\allure-report")
    logging.info(allureDir)



