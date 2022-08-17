# utf-8=coding

import os
import logging
import colorlog


# 将log同时输出到 控制台和本地文件

#   配置log,logger是日志对象，handler是流处理器，console是控制台输出

log_colors_config = {
    # 终端输出日志颜色配置
    'DEBUG': 'white',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

def Logger(log_filename):
    # 创建文件目录
    if not os.path.exists(log_filename): os.mkdir(log_filename)

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    # 获取logger对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建一个handler,输出到 日志文件
    LOGFILE_FORMAT = "[%(asctime)s]-[%(levelname)s] %(message)s"
    outFile = logging.FileHandler(log_filename)
    outFile.setFormatter(logging.Formatter(fmt=LOGFILE_FORMAT, datefmt=DATE_FORMAT))
    logger.addHandler(outFile)

    # 创建一个handler，输出到 控制台
    LOG_FORMAT = "[%(log_color)s%(asctime)s]-[%(levelname)s] %(message)s"   # 添加了颜色
    outTerminal = logging.StreamHandler()

    # 控制台添加颜色
    TerminalColors = colorlog.ColoredFormatter(log_colors=log_colors_config, fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
    outTerminal.setFormatter(TerminalColors)
    logger.addHandler(outTerminal)

    return logger


if __name__ == "__main__" :
    Logger(r"D:\pycharm\20220412\webuitest\report\my.log").info("123")
    Logger(r"D:\pycharm\20220412\webuitest\report\my.log").warning("1234")



