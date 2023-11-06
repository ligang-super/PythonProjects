# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys

sys.argv.append(os.getcwd())
sys.path.append(os.getcwd() + '/../../')

import time
import datetime
import exifread
import shutil
from collections import defaultdict
from PIL import Image
from PIL.ExifTags import TAGS

from common import common_file

from common import common_image

def deal_image_20230809_rename():

    src_path = 'E:/Images/可乐芭学园毕业旅行'
    dirs, files = common_file.getAllSubs(src_path)

    for old_name in files:
        if old_name.endswith(".tmp"):
            new_name = old_name.replace(".tmp", ".jpg")
            os.rename(old_name, new_name)





if __name__ == '__main__':
    print("Hello")
    deal_image_20230809_rename()




