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
import enum
from collections import defaultdict
from common import common_file
from common.common_file_ext import FileType, COMMON_FILE_EXTENSION_TYPE


def __get_extensions():
    src_paths = ['G:/', 'U:/', 'V:/', 'W:/',]

    s = set()

    for src_path in src_paths:
        dirs, files = common_file.getAllSubs(src_path)
        for fpath in files:
            fname = os.path.basename(fpath)
            l = fname.split(".")
            if len(l) > 1:
                ext = l[-1].lower()
                s.add(ext)

    for ext in s:
        if common_file.get_file_type(ext) == FileType.UNKNOWN:
            print("'" + ext + "': " + "FileType." + ",")


def statistic_directory(dir):
    dir = dir.replace('\\', '/')
    if not dir.endswith('/'):
        dir += '/'

    dirs, files = common_file.getAllSubs(dir)

    res_dict = {}
    total_count = 0
    total_size = 0
    for fpath in files:
        fname = os.path.basename(fpath)
        ext_string, ext_type = common_file.get_ext_of_file(fname)

        if ext_type not in res_dict:
            res_dict[ext_type] = {
                "files": [],
                "file_size": 0,
                "file_count": 0
            }

        res_dict[ext_type]["files"].append(fname)
        fsize = common_file.getFileSize(fpath)
        res_dict[ext_type]["file_size"] += fsize
        res_dict[ext_type]["file_count"] += 1
        total_size += fsize
        total_count += 1

    res_dict["total_count"] = total_count
    res_dict["total_size"] = total_size

    return res_dict


def statdict_total_size_satisfied(stat_dict):
    # 文件夹总大小是否大于1M
    total_size = stat_dict.get("total_size", 0)
    total_count = stat_dict.get("total_count", 0)
    if total_size > 1 * 1024 * 1024:
        return True
    return False


def statdict_doc_video_audio_image_size_satisfied(stat_dict):
    # 文档+视频+音频+图像总大小是否大于1M
    stat_doc = stat_dict.get(FileType.DOC, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })
    stat_video = stat_dict.get(FileType.VIDEO, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })
    stat_img = stat_dict.get(FileType.IMAGE, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })
    stat_audio = stat_dict.get(FileType.AUDIO, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })

    dvia_size = stat_doc["file_size"] + \
                stat_video["file_size"] + \
                stat_img["file_size"] + \
                stat_audio["file_size"]

    if dvia_size > 1 * 1024 * 1024:
        return True
    return False


def statdict_almost_video(stat_dict):
    # 文件夹中，几乎只有视频，其它文件没有或很少
    stat_doc = stat_dict.get(FileType.DOC, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })
    stat_video = stat_dict.get(FileType.VIDEO, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })
    stat_img = stat_dict.get(FileType.IMAGE, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })
    stat_audio = stat_dict.get(FileType.AUDIO, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })

    video_count = stat_video["file_count"]
    dvia_count = video_count + \
                 stat_doc["file_count"] + \
                 stat_img["file_count"] + \
                 stat_audio["file_count"]

    if video_count == dvia_count:
        return True
    return False





def move_downloaded_files(src_path, dest_path):
    src_path = src_path.replace('\\', '/')
    if not src_path.endswith('/'):
        src_path += '/'
    dest_path = dest_path.replace('\\', '/')
    if not dest_path.endswith('/'):
        dest_path += '/'

    for _item in os.listdir(src_path):
        dir_name = _item
        _path = src_path + dir_name
        if os.path.isdir(_path):
            dir_path = _path + "/"

            stat_dict = statistic_directory(dir_path)

            if not statdict_total_size_satisfied(stat_dict):
                print(dir_path, "total size not satisfied")
                shutil.rmtree(dir_path)
                continue

            if not statdict_doc_video_audio_image_size_satisfied(stat_dict):
                print(dir_path, "doc+video+img+audio size not satisfied")
                shutil.rmtree(dir_path)
                continue

            if statdict_almost_video(stat_dict):
                #print(dir_path, "almost video")
                fname1 = stat_dict[FileType.VIDEO]["files"][0]

                stat_dir = count_str(_item)
                stat_file = count_str(fname1)

                #print(stat_dir, stat_file)

                if stat_file["chinese_count"] > 0:
                    print(dir_name, fname1)
                    shutil.move(dir_path + fname1, dest_path + fname1)
                else:
                    _file_name, _file_ext = common_file.get_filename_and_extension(fname1)
                    print(dir_name, _file_name, _file_ext)

                    shutil.move(dir_path + fname1, dest_path + dir_name + "." + _file_ext)


                continue


        else:
            pass



def deal_download_20230325_move():
    src_path = 'F:/迅雷下载'
    dest_path = 'F:/2'
    move_downloaded_files(src_path, dest_path)







if __name__ == '__main__':
    print("Hello", os.path.basename(__file__))
    deal_download_20230325_move()
    #__get_extensions()

    #count_str("Herio is 一个男孩")




