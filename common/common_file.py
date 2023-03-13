# -*- coding:utf-8 -*-
# __author__='LiGang'

import os
import sys

sys.path.append(os.getcwd() + '/../')

import time
import datetime
import win32file
import exifread
import eyed3
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from collections import defaultdict

sys.argv.append(os.getcwd())

GET_SIZE_TOTAL_COST = 0.0

def getFileSize(file_path, stat_cost=True):
    if stat_cost:
        global GET_SIZE_TOTAL_COST
        t1 = time.time()

        file_size = os.path.getsize(file_path)
        GET_SIZE_TOTAL_COST += (time.time() - t1)
    else:
        file_size = os.path.getsize(file_path)

    return file_size


def getAllSubs(src_path):
    '''
    获取路径下所有的文件夹和文件，
    params:
        src_path: 待获取的路径
    ret:
        dirs, files: 路径list和文件list
    '''

    src_path = src_path.replace('\\', '/')
    if not src_path.endswith('/'):
        src_path += '/'

    all_files = []
    all_dirs = []
    for root, dirs, files in os.walk(src_path):
        root = root.replace('\\', '/')
        if not root.endswith('/'):
            root += '/'
        for file in files:
            all_files.append(root + file)
        for dir in dirs:
            all_dirs.append(root + dir)
    return all_dirs, all_files





def getSameSizeFiles(src_path):
    all_dirs, all_files = getAllSubs(src_path)

    d = defaultdict(list)

    for file_path in all_files:
        file_size = getFileSize(file_path)
        d[file_size].append(file_path)

    for file_size, file_paths in d.items():
        if len(file_paths) > 1:
            print(file_paths)




def getExif(file_apth):
    #path1 = 'E:/Images/Present/Current_iPhone11/图片/2022-09-07 - 2022-11-09/2022-10-13 001.JPG'
    #path2 = 'E:/Images/Present/Current_iPhone11/图片/2022-09-07 - 2022-11-09/2022-10-17 015.PNG'
    #path3 = 'E:/Images/Present/Current_iPhone11/图片/2022-09-07 - 2022-11-09/2022-10-15 015.GIF'
    #path4 = 'E:/Images/Present/Current_iPhone11/图片/2022-09-07 - 2022-11-09/2022-11-08 032.MOV'
    f = open(file_apth, 'rb')

    tags = exifread.process_file(f)
    f.close()
    #print("tags=", tags)
    # 打印所有照片信息，会以键值对的方法保存
    #for tag in tags.keys():
    #    print("Key: {0}, value {1}".format(tag, tags[tag]))

    # 打印照片其中一些信息
    #print('拍摄时间：', tags['EXIF DateTimeOriginal'])
    #print('照相机制造商：', tags['Image Make'])
    #print('照相机型号：', tags['Image Model'])
    #print('照片尺寸：', tags['EXIF ExifImageWidth'], tags['EXIF ExifImageLength'])

    return tags.get('Image Model')

def getExifByPil(file_apth):
    img = Image.open(file_apth)

    ret = {}
    if hasattr(img, '_getexif'):
        exifinfo = img._getexif()
        if exifinfo:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value

    img.close()
    return ret


def GetWin32Times(filePath):
    ctime = os.path.getctime(filePath)
    ctime_string = datetime.datetime.fromtimestamp(ctime)

    mtime = os.path.getmtime(filePath)
    mtime_string = datetime.datetime.fromtimestamp(mtime)

    atime = os.path.getatime(filePath)
    atime_string = datetime.datetime.fromtimestamp(atime)

    return ctime_string.strftime("%Y-%m-%d %H:%M:%S"), \
           atime_string.strftime("%Y-%m-%d %H:%M:%S"), \
           mtime_string.strftime("%Y-%m-%d %H:%M:%S")


def SynFileWin32Times(srcFile, destFile):
    old_ctime_string, old_atime_string, old_mtime_string = GetWin32Times(srcFile)
    new_ctime = datetime.datetime.strptime(old_ctime_string, "%Y-%m-%d %H:%M:%S")
    new_atime = datetime.datetime.strptime(old_atime_string, "%Y-%m-%d %H:%M:%S")
    new_mtime = datetime.datetime.strptime(old_mtime_string, "%Y-%m-%d %H:%M:%S")

    handle = win32file.CreateFile(destFile, win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                                  0, None, win32file.OPEN_EXISTING, 0, 0)
    win32file.SetFileTime(handle, new_ctime, new_atime, new_mtime)
    win32file.CloseHandle(handle)



if __name__ == '__main__':
    pass

    #getExif()
    #getFiles()

    #path1 = 'E:/Images/Present/Current_iPhone11/图片/2022-09-07 - 2022-11-09/2022-10-13 001.JPG'
    #path2 = 'E:/Images/Present/Current_iPhone11/图片/2022-09-07 - 2022-11-09/2022-10-17 015.PNG'
    #path3 = 'E:/Images/Present/Current_iPhone11/图片/2022-09-07 - 2022-11-09/2022-10-15 015.GIF'
    #path4 = 'E:/Images/Present/Current_iPhone11/图片/2022-09-07 - 2022-11-09/2022-11-08 032.MOV'
    #getExifByPil(path1)

    #getSize()

    #all_dirs, all_files = getAllSubs('E:/Images/李其乐')
    #print(all_dirs)
    #print(all_files)

    #getSameSizeFiles('E:/Images/李其乐/ALL_IMAGES')
    #getSameSizeFiles('E:/Images/History')

    #changeMp3Tag(dirpath="E:/Music/录音笔/高效能人士的七个习惯")

    #path = "E:/Music/录音笔/《人生只有一件事》-金惟纯/000. 自序 学怎么活.mp3"
    #audiofile = eyed3.load(path)
    #print(os.stat(path))



