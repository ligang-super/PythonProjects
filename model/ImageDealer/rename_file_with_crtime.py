import datetime
import os
import time


def rename_as_crtime(dir=''):
    if not dir.endswith("/") and not dir.endswith("\\"):
        dir += '/'
    filelist = os.listdir(dir)
    print('\"%s\" has %d files' % (dir, len(filelist)))


    for fname in filelist:
        if len(fname) > 8 and fname[4] == '-' and fname[7] == '-':
            continue

        old_file = dir + fname

        t = os.path.getmtime(old_file)
        timeStruce = time.localtime(t)
        #str_crtime = time.strftime('%Y-%m-%d %H:%M:%S', timeStruce)
        str_crtime = time.strftime('%Y-%m-%d', timeStruce)
        print(str_crtime)

        new_file = dir + str_crtime + '_' + fname

        os.rename(old_file, new_file)

import os
from PIL import Image
from pillow_heif import register_heif_opener
register_heif_opener()
import glob
import os

def heic2jpg(dir=''):
    if not dir.endswith("/") and not dir.endswith("\\"):
        dir += '/'
    filelist = os.listdir(dir)
    print('\"%s\" has %d files' % (dir, len(filelist)))


    for fname in filelist:

        if not fname.endswith('.HEIC') and not fname.endswith('.heic'):
            continue

        _file = dir + fname
        print(_file)

        image = Image.open(_file)

        if '.HEIC' in _file:
            jpgname = _file.replace(".HEIC", '.jpg')
        else:
            jpgname = _file.replace(".heic", '.jpg')

        image.save(jpgname, format="jpeg")

        os.remove(_file)



#rename_as_crtime('E:/Images/2023-01-19')
heic2jpg('E:/Images/2023-01-19')

