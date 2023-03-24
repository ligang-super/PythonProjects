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

from common import common_image

def dealImage_20230212_sync():
    ignore_dirs = ['E:/Images/Web/', 'E:/Images/Present/']
    src_path = 'E:/Images/李其乐'
    dest_path = 'F:/Images/李其乐'
    diffs = common_image.CmpImageDirectory(src_path, dest_path, ignore=ignore_dirs)
    common_image.PrintDiffs(diffs, print_mode='write', data_mode='dest')
    #common_image.syn_files(src_path, dest_path, ignore=ignore_dirs)

    # shutil.copytree('E:/Images/History/{2022.11.06}_北京马拉松', 'F:/Images/History/{2022.11.06}_北京马拉松')

def dealImage_20230219_sync():
    #ignore_dirs = ['E:/Images/Web/', 'E:/Images/Present/']
    ignore_dirs = []
    src_path = 'E:/Images/Web/_sync'
    dest_path = 'F:/Images/Web/_sync'
    diffs = common_image.CmpImageDirectory(src_path, dest_path, ignore=ignore_dirs)
    common_image.PrintDiffs(diffs, print_mode='print', data_mode='dest')
    common_image.SynFiles(src_path, dest_path, ignore=ignore_dirs)

    # shutil.copytree('E:/Images/History/{2022.11.06}_北京马拉松', 'F:/Images/History/{2022.11.06}_北京马拉松')

if __name__ == '__main__':
    #dealImage_20230219_sync()
    print("Hello")
    srcFilePath = "C:/Users/Administrator/Pictures/我的照片/iphone6s plus/FNMZ1214.JPG"
    destFilePath = "C:/Users/Administrator/Pictures/我的照片/iphone6s plus/FNMZ12142.JPG"
    common_image.SynFileWin32Times(srcFilePath, destFilePath)



