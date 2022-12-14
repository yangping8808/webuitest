# coding=utf-8

import time
import random
import string
import sys
import os

'''获取当前时间'''


def localTime():
    # time.time()   获取当前时间戳，从1970年1月1日0时0份0秒为计时起点
    # time.localtime()   结果是时间元组
    # time.strftime("%Y-%m-%d %H-%M:%S",time.localtime())  时间元组格式的时间以format的形式输出，format的形式可以自定义
    # print(time.strftime("[%Y-%m-%d %H-%M-%S]", time.localtime()))
    return time.strftime("[%Y-%m-%d-%H-%M-%S]", time.localtime())


'''获取随机字母数字'''


def randomStrInt(num):
    # random.randrange(start, stop, step) 返回指定范围[start, stop)内，按照指定步长step递增的一个随机数；
    # random.randint(a, b)  返回指定范围[a, b]内的一个随机整数
    # random.choice(seq) 从给定序列seq中返回一个随机值，seq可以是列表、元组、字符串
    str = string.ascii_letters + string.digits
    # print(random.sample(str,5))   #从序列中随机生成5个
    print(''.join(random.choice(str) for i in range(num)))
    return ''.join(random.choice(str) for i in range(num))


'''获取随机数字'''


def randomInt(num):
    return ''.join((random.choice(string.digits)) for i in range(num))


'''获取随机长度的字符串'''


def randomString(num):
    return ''.join(random.choice(string.ascii_letters) for i in range(num))


'''获取当前项目路径'''



def get_project_rootpath():
    """
    获取项目根目录。此函数的能力体现在，不论当前module被import到任何位置，都可以正确获取项目根目录
    :return:
    """
    path = os.path.realpath(os.curdir)
    while True:
        # PyCharm项目中，'.idea'是必然存在的，且名称唯一
        if '.idea' in os.listdir(path):
            return path
        path = os.path.dirname(path)


'''创建文件夹'''


def createDir(path):
    return get_project_rootpath() + '\\' + path + '\\' + localTime()


if __name__ == '__main__':
    print(get_project_rootpath())
