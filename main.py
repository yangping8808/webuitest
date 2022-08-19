import os
import sys
import logging
import common.base
import pytest

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # D:\pycharm\20220412\webuitest

if __name__ == '__main__':
    allureDir = common.base.createDir(r"report\allure-report")
    logging.info(allureDir)
    # 生成测试报告json
    pytest.main(["-s", "-q", "testcase/test_fixture.py", "--alluredir", allureDir])
    # 将测试报告转为html格式
    os.system("allure generate %s -o %s --clean" % (allureDir, allureDir + r'\html'))
    # os.system("allure open -h 127.0.0.1 -p 8883 %s" % (allureDir + r'\html'))
