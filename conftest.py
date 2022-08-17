import logging
import time
import pytest
from selenium import webdriver


# @pytest.fixture(scope="function", name='driver', params=[webdriver.Chrome()], ids=['Chrome'])
@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome()
    logging.info("****打开浏览器****")
    driver.get("https://www.baidu.com")
    yield driver

    def quitBrowser():
        driver.quit()
        logging.info("****关闭浏览器****")

    request.addfinalizer(quitBrowser)
