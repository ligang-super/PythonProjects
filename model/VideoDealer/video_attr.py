# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys

import time
import datetime
import exifread
import shutil
import enum
from collections import defaultdict
from common import common_file, common_string
from common.common_file_ext import FileType, COMMON_FILE_EXTENSION_TYPE


import json
from pymediainfo import MediaInfo



# ****** Copyright (C)2020 Aaron. All Rights Reserved ****** END OF FILE ******* #


if __name__ == '__main__':
    print("Hello", os.path.basename(__file__))

    file_path = 'E:/GoPro/历史文件/2022-08-29 送可乐上学01.MP4'  # 文件的绝对路径
    media_info = MediaInfo.parse(file_path)
    data = media_info.to_json()
    data = json.loads(data)
    data = data['tracks']
    print(data)
    #print("视频标题：", data[0]['title'])
    #print("视频备注：", data[0]['comment'])

