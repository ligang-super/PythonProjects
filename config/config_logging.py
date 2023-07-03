# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys
import re
import logging
import logging.handlers


def setup_logger(file_name, log_path, logger_name="PythonProject", console_output=False):
    # create logger
    if not log_path.startswith('/'):
        log_path = '/' + log_path
    log_path = log_path.replace('\\', '/')
    if sys.platform == "win32":
        # windows环境
        log_path = "D:/code/log/" + log_path
    elif sys.platform == "linux":
        # linux环境
        log_path = "/var/log" + log_path
    else:
        log_path = "./log" + log_path

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # create directory
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')

    if console_output:
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        logger.addHandler(ch)

    log_name = os.path.join(log_path, file_name)

    fh = logging.handlers.TimedRotatingFileHandler(log_name, when="H", interval=1, backupCount=24 * 7,
                                                   encoding='utf-8')
    fh.suffix = "%Y-%m-%d_%H.log"  # 日志文件后缀
    fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}.log$")
    fh.setLevel(logging.DEBUG)  # 设置输出到日志文件等级
    fh.setFormatter(formatter)  # 设置写到日志文件格式
    logger.addHandler(fh)

    # test
    #logger.debug('debug message')
    #logger.info('info message')
    #logger.warning('warn message')
    #logger.error('error message')

    return logger

