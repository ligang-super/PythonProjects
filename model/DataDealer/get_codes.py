# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys
import time
import datetime
import exifread
import shutil
from collections import defaultdict
from PIL import Image
from PIL.ExifTags import TAGS

from common import common_image, common_file


def get_dir_codes(dir_paths):
    dirs = []
    files = []
    for dir_path in dir_paths:
        _dirs, _files = common_file.getAllSubs(dir_path)
        dirs += _dirs
        files += _files

    res_file = "code.txt"
    with open(res_file, "w") as fw:
        for file_path in files:
            if file_path.endswith(".py"):
                new_file_path = file_path.replace("D:/code/", "")
                fw.write(new_file_path + '\n')
                with open(file_path, "rb") as fr:
                    fw.write(fr.read().decode('utf-8') )
                    fw.write('\n')

    print("write %s finish" % res_file)


if __name__ == '__main__':
    dir_path1 = "D:/code/springer-scene-recognition"
    dir_path2 = "D:/code/springer-ai-server/springer-ai-server/SceneRec"
    dir_path3 = "D:/code/springer-ai-server/springer-ai-server/PopupRec"
    get_dir_codes([dir_path1, dir_path2, dir_path3])


