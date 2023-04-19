# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys

sys.argv.append(os.getcwd())
sys.path.append(os.getcwd() + '/../../')

from config import config_logging

if __name__ == '__main__':
    config_logging.setup_logger("test", "./")
    pass