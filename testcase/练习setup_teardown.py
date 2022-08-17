# coding=utf-8


import logging


def setup_module():
    logging.info("setup_module")


def teardown_module():
    logging.info("teardown_module")


def setup_function():
    logging.info("setup_function")


def teardown_function():
    logging.info("teardown_function")


def test_01():
    logging.info("test_01")


def test_02():
    logging.info("test_02")


class Test_class1:

    def setup_class(self):
        logging.info("Test_class1   setup_class")

    def teardown_class(self):
        logging.info("Test_class1   teardown_class")

    def setup_method(self):
        logging.info("Test_class1   setup_method")

    def teardown_method(self):
        logging.info("Test_class1   teardown_method")

    def test_03(self):
        logging.info("test_03")

    def test_04(self):
        logging.info("test_04")


class Test_class2:

    def setup_class(self):
        logging.info("Test_class2   setup_class")

    def teardown_class(self):
        logging.info("Test_class2   teardown_class")

    def setup_method(self):
        logging.info("Test_class2   setup_method")

    def teardown_method(self):
        logging.info("Test_class2   teardown_method")

    def test_05(self):
        logging.info("test_05")

    def test_06(self):
        logging.info("test_06")
