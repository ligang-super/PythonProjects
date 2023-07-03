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


@enum.unique
class StatDictType(enum.Enum):
    NONE = 0  # 正常
    TOTAL_SIZE_NOT_SATISFIED = 1  # 文件夹总大小，小于1M
    DOC_VIDEO_AUDIO_IMAGE_SIZE_NOT_SATISFIED = 2  # 文档+视频+音频+图像总大小，小于1M
    ONLY_1_VIDEO = 3  # 文件夹中，只有一个视频，其它文件没有或很少
    ONLY_1_VIDEO_AND_LESS_IMAGES = 4  # 文件夹中，只有一个视频和一些图片，图片数 < 5
    ONLY_1_VIDEO_AND_MORE_IMAGES = 5  # 文件夹中，只有一个视频和一些图片，图片数 >= 5


def __get_extensions():
    src_paths = ['G:/', 'U:/', 'V:/', 'W:/', ]

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
        ext_string, ext_type = common_file.get_ext_and_filetype(fname)

        if ext_type not in res_dict:
            res_dict[ext_type] = {
                "files": [],
                "file_size": 0,
                "file_count": 0
            }

        res_dict[ext_type]["files"].append(fpath)
        fsize = common_file.getFileSize(fpath)
        res_dict[ext_type]["file_size"] += fsize
        res_dict[ext_type]["file_count"] += 1
        total_size += fsize
        total_count += 1

    res_dict["total_count"] = total_count
    res_dict["total_size"] = total_size

    return res_dict


def statdict_satisfied(stat_dict):
    # 文件夹总大小是否大于1M
    total_size = stat_dict.get("total_size", 0)
    total_count = stat_dict.get("total_count", 0)
    if total_size < 1 * 1024 * 1024:
        return StatDictType.TOTAL_SIZE_NOT_SATISFIED

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
    stat_gif = stat_dict.get(FileType.GIF, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })
    stat_audio = stat_dict.get(FileType.AUDIO, {
        "files": [],
        "file_size": 0,
        "file_count": 0
    })

    if stat_doc["file_size"] + \
            stat_video["file_size"] + \
            stat_img["file_size"] + \
            stat_gif["file_size"] + \
            stat_audio["file_size"] < 1 * 1024 * 1024:
        return StatDictType.DOC_VIDEO_AUDIO_IMAGE_SIZE_NOT_SATISFIED

    if stat_video["file_count"] == 1 and \
            stat_doc["file_count"] == 0 and \
            stat_img["file_count"] == 0 and \
            stat_gif["file_count"] == 0 and \
            stat_audio["file_count"] == 0:
        return StatDictType.ONLY_1_VIDEO

    if stat_video["file_count"] == 1 and \
            stat_doc["file_count"] == 0 and \
            stat_img["file_count"] + stat_gif["file_count"] < 5 and \
            stat_audio["file_count"] == 0:
        return StatDictType.ONLY_1_VIDEO_AND_LESS_IMAGES

    if stat_video["file_count"] == 1 and \
            stat_doc["file_count"] == 0 and \
            stat_img["file_count"] + stat_gif["file_count"] >= 5 and \
            stat_audio["file_count"] == 0:
        return StatDictType.ONLY_1_VIDEO_AND_MORE_IMAGES

    return StatDictType.NONE





def move_downloaded_files(src_path, dest_path, evaluate=True):
    src_path = src_path.replace('\\', '/')
    if not src_path.endswith('/'):
        src_path += '/'
    dest_path = dest_path.replace('\\', '/')
    if not dest_path.endswith('/'):
        dest_path += '/'

    delete_dirs = []
    move_dirs = []
    other_dirs = []

    delete_files = []
    move_files = []

    for _item in os.listdir(src_path):
        dir_name = _item  # 当前处理的文件夹名
        _path = src_path + dir_name  # 当前处理的文件夹路径，尾部不带/

        if os.path.isdir(_path):
            dir_path = _path + "/"  # 当前处理的文件夹路径，尾部带/

            stat_dict = statistic_directory(dir_path)
            stat_type = statdict_satisfied(stat_dict)

            # 文件夹总大小是否大于1M, 不满足条件, 直接删除
            if stat_type == StatDictType.TOTAL_SIZE_NOT_SATISFIED:
                print(dir_path, "total size not satisfied")
                if evaluate:
                    delete_dirs.append({"dir_src": dir_path, "reason": "total size not satisfied"})
                else:
                    shutil.rmtree(dir_path)
                continue

            # 文档+视频+音频+图像总大小是否大于1M, 不满足条件, 直接删除
            if stat_type == StatDictType.DOC_VIDEO_AUDIO_IMAGE_SIZE_NOT_SATISFIED:
                print(dir_path, "doc+video+img+audio size not satisfied")
                if evaluate:
                    delete_dirs.append({"dir_src": dir_path, "reason": "doc+video+img+audio size not satisfied"})
                else:
                    shutil.rmtree(dir_path)
                continue

            if stat_type == StatDictType.ONLY_1_VIDEO or stat_type == StatDictType.ONLY_1_VIDEO_AND_LESS_IMAGES:
                print(dir_path, "only 1 video and not images or less images")
                fpath1 = stat_dict[FileType.VIDEO]["files"][0]
                fname1 = os.path.basename(fpath1)

                stat_dir = common_string.count_str(_item)
                stat_file = common_string.count_str(fname1)

                # print(stat_dir, stat_file)

                if stat_file["chinese_count"] > 0:
                    print(dir_name, fname1)
                    if evaluate:
                        move_dirs.append(
                            {"dir_src": fpath1, "dir_dest": dest_path + fname1, "reason": "statdict_only_1_video"})
                    else:
                        shutil.move(fpath1, dest_path + fname1)

                else:
                    _file_name, _file_ext = common_file.get_filename_and_extion(fname1)
                    print(dir_name, _file_name, _file_ext)
                    if evaluate:
                        move_dirs.append(
                            {"dir_src": dir_path + fname1, "dir_dest": dest_path + dir_name + "." + _file_ext,
                             "reason": "statdict_only_1_video"})
                    else:
                        shutil.move(dir_path + fname1, dest_path + dir_name + "." + _file_ext)
                continue

            if stat_type == StatDictType.ONLY_1_VIDEO_AND_MORE_IMAGES:
                print(dir_path, "only 1 video and more images")
                dir_dest = dest_path + dir_name
                # TODO: 增加移动视频和图片到目标目录下
                pass

            other_dirs.append({"dir_src": _path})
        else:
            ext_string, ext_type = common_file.get_ext_and_filetype(_path)
            if ext_type == FileType.VIDEO:
                _new_path = dest_path + dir_name

                if evaluate:
                    move_files.append({"dir_src": _path, "dir_dest": _new_path,
                                       "reason": "is video"})
                else:
                    shutil.move(_path, _new_path)

            else:
                if evaluate:
                    delete_files.append({"dir_src": _path,
                                         "reason": "is not video"})
                else:
                    os.remove(_path)

    if evaluate:
        for i in move_files:
            print("MOVE FILES:", i)
        for i in delete_files:
            print("DELETE FILES:", i)
        for i in move_dirs:
            print("MOVE DIRS:", i)
        for i in delete_dirs:
            print("DELETE DIRS:", i)
        for i in other_dirs:
            print("OTHER DIRS:", i)


def deal_download_20230325_move():
    src_path = 'F:/迅雷下载'
    dest_path = 'F:/2'
    move_downloaded_files(src_path, dest_path)


if __name__ == '__main__':
    print("Hello", os.path.basename(__file__))

    #src_path = 'F:/迅雷下载'
    #dest_path = 'F:/1'
    #move_downloaded_files(src_path, dest_path, evaluate=False)

    src_path = 'D:/场景识别/test2/test.txt'
    dest_path = 'D:/场景识别/test2/test/test100.txt'
    shutil.move(src_path, dest_path)

