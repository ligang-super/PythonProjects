# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys

sys.argv.append(os.getcwd())
sys.path.append(os.getcwd() + '/../../')

from config import config_logging

if __name__ == '__main__':
    logger1 = config_logging.setup_logger(file_name="test1", log_path="./", logger_name='my1', console_output=True)
    logger2 = config_logging.setup_logger(file_name="test1", log_path="./", logger_name='my2', console_output=True)
    logger1.warning("warn1")
    logger2.warning("warn2")

    try:
        a = 1 / 0
    except Exception as e:
        logger1.error(e, exc_info=True)


    pass