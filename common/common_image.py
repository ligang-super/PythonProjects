# -*- coding:utf-8 -*-
# __author__='LiGang'

import os
import sys

sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/../')


import chardet
import exifread
import eyed3
import shutil
from collections import defaultdict
from PIL import Image
from PIL.ExifTags import TAGS

from common.common_file import getExifByPil, getAllSubs


def MoveShotImage(src_path, dest_path):
    src_path = src_path.replace('\\', '/')
    dest_path = dest_path.replace('\\', '/')

    if not src_path.endswith('/'):
        src_path += '/'
    if not dest_path.endswith('/'):
        dest_path += '/'

    all_dirs, all_files = getAllSubs(src_path)
    print('file count=%d' % len(all_files))

    for file in all_files:
        lower_file = file.lower()
        if lower_file.endswith('.jpg') or lower_file.endswith('.png'):
            exifinfo = getExifByPil(file)
            model = exifinfo.get('Model', '').lower()
            if 'iphone' in model:
                print(file, model)
                new_path = dest_path + model
                if not os.path.exists(new_path):
                    os.mkdir(new_path)

                shutil.move(file, new_path + '/' + os.path.basename(file))

            else:
                print(file, exifinfo)

            continue


def CmpImageDirectory(src, dest, mode='default', ignore=[]):
    '''
    对比两个目录下不同的文件目录和文件名
    :param src: 源目录
    :param dest: 目标目录
    :param mode:
    :param ignore:
    default: just show differences, will not change anything
    :return: diffs
    '''
    src = src.replace('\\', '/')
    if not src.endswith('/'):
        src += '/'
    dest = dest.replace('\\', '/')
    if not dest.endswith('/'):
        dest += '/'
    _ignore = []
    for _ig_dir in ignore:
        _ig_dir = _ig_dir.replace('\\', '/')
        if not _ig_dir.endswith('/'):
            _ig_dir += '/'
        _ignore.append(_ig_dir)
    ignore = _ignore

    if src in ignore or dest in ignore:
        return []

    dirs = []
    l = [['', '']]

    filelist1 = os.listdir(src)
    filelist2 = os.listdir(dest)
    s1 = set(filelist1)
    s2 = set(filelist2)

    has_file = False
    has_dir = False
    is_same = True

    diffs = []
    d = {
        'src': src,
        'dest': dest,
        'src_miss':     {'dir_cnt': 0, 'file_cnt': 0, 'dir_list': [], 'file_list': []},
        'dest_miss':    {'dir_cnt': 0, 'file_cnt': 0, 'dir_list': [], 'file_list': []},
        'diff':         {'dir_cnt': 0, 'file_cnt': 0, 'dir_list': [], 'file_list': []},
        'format_error': {'error_cnt': 0, 'error_list': []}
         }
    todolist = set()
    for f in filelist1:
        if f == 'Thumbs.db':
            continue
        if src + f + '/' in ignore:
            continue
        if f not in s2:
            if os.path.isdir(src + f):
                d['dest_miss']['dir_cnt'] += 1
                d['dest_miss']['dir_list'].append(f)
            else:
                d['dest_miss']['file_cnt'] += 1
                d['dest_miss']['file_list'].append(f)
        else:
            todolist.add(f)

    for f in filelist2:
        if f == 'Thumbs.db':
            continue
        if dest + f + '/' in ignore:
            continue
        if f not in s1:
            if os.path.isdir(dest + f):
                d['src_miss']['dir_cnt'] += 1
                d['src_miss']['dir_list'].append(f)
            else:
                d['src_miss']['file_cnt'] += 1
                d['src_miss']['file_list'].append(f)
        else:
            todolist.add(f)

    for f in todolist:
        if os.path.isdir(src+f):
            if os.path.isdir(dest+f):
                tmp_diff = CmpImageDirectory(src + f, dest + f, mode, ignore)
                if tmp_diff:
                    d['diff']['dir_cnt'] += 1
                    d['diff']['dir_list'].append(f)
                    diffs = diffs + tmp_diff

            else:
                d['format_error']['error_cnt'] += 1
                d['format_error']['error_list'].append(f)
        else:
            if os.path.isdir(dest+f):
                d['format_error']['error_cnt'] += 1
                d['format_error']['error_list'].append(f)

    if d['src_miss']['dir_cnt'] > 0 or \
        d['dest_miss']['dir_cnt'] > 0 or \
        d['src_miss']['file_cnt'] > 0 or \
        d['dest_miss']['file_cnt'] > 0 or \
        d['diff']['dir_cnt'] > 0 or \
        d['diff']['file_cnt'] >0 or\
        d['format_error']['error_cnt'] > 0:
        diffs = [d] + diffs

    return diffs


def PrintDiffs(diffs, print_mode='print', data_mode='dest'):
    '''
        打印diff
        :diffs
        :param print_mode: print: 输出到中断， write: 写入到diff.txt文件
        :param data_mode: src: 只保留 src中缺失的图片， dest: 只保留dest缺失的文件， all: 保留所有

        :return:
    '''
    info = ''


    '''
    if data_mode not in 'all':
        diffs.reverse()

        new_diff = []
        for diff in diffs:
            if data_mode == 'src' and (diff['src_miss']['dir_cnt'] > 0 or diff['src_miss']['file_cnt'] > 0):
                line = '    %s miss %d dirs, %d files: \n' % (
                diff['src'], diff['src_miss']['dir_cnt'], diff['src_miss']['file_cnt'])
                for _dir in diff['src_miss']['dir_list']:
                    line += '    [DIR]: %s\n' % _dir
                for _file in diff['src_miss']['file_list']:
                    line += '    [FILE]: %s\n' % _file

                info += line
            if data_mode in ('dest', 'all') and (diff['dest_miss']['dir_cnt'] > 0 or diff['dest_miss']['file_cnt'] > 0):
                line = '    %s miss %d dirs, %d files: \n' % (
                diff['dest'], diff['dest_miss']['dir_cnt'], diff['dest_miss']['file_cnt'])

                for _dir in diff['dest_miss']['dir_list']:
                    line += '    [DIR]: %s\n' % _dir
                for _file in diff['dest_miss']['file_list']:
                    line += '    [FILE]: %s\n' % _file

                info += line
    '''

    for diff in diffs:

        if data_mode == 'all':
            line = '%s <-> %s\n' % (diff['src'], diff['dest'])
            info += line
        elif data_mode == 'dest':
            if diff['dest_miss']['dir_cnt'] > 0 or diff['dest_miss']['file_cnt'] > 0:
                line = '%s -> %s\n' % (diff['src'], diff['dest'])
                info += line
            else:
                continue
        elif data_mode == 'src':
            if diff['src_miss']['dir_cnt'] > 0 or diff['src_miss']['file_cnt'] > 0:
                line = '%s <- %s\n' % (diff['src'], diff['dest'])
                info += line
            else:
                continue

        if data_mode in ('src', 'all') and (diff['src_miss']['dir_cnt'] > 0 or diff['src_miss']['file_cnt'] > 0):
            line = '    %s miss %d dirs, %d files: \n' % (diff['src'], diff['src_miss']['dir_cnt'], diff['src_miss']['file_cnt'])
            for _dir in diff['src_miss']['dir_list']:
                line += '    [DIR]: %s\n' % _dir
            for _file in diff['src_miss']['file_list']:
                line += '    [FILE]: %s\n' % _file

            info += line
        if data_mode in ('dest', 'all') and (diff['dest_miss']['dir_cnt'] > 0 or diff['dest_miss']['file_cnt'] > 0):
            line = '    %s miss %d dirs, %d files: \n' % (diff['dest'], diff['dest_miss']['dir_cnt'], diff['dest_miss']['file_cnt'])

            for _dir in diff['dest_miss']['dir_list']:
                line += '    [DIR]: %s\n' % _dir
            for _file in diff['dest_miss']['file_list']:
                line += '    [FILE]: %s\n' % _file

            info += line
        if diff['diff']['dir_cnt'] > 0:
            line = '    HAVE %d different dirs: \n' % diff['diff']['dir_cnt']
            for _dir in diff['diff']['dir_list']:
                line += '    [DIR]: %s\n' % _dir

            info += line

        if diff['format_error']['error_cnt'] > 0:
            line = '    HAVE %d format errors: \n' % diff['format_error']['error_cnt']
            for _dir in diff['format_error']['error_list']:
                line += '    [ERROR]: %s\n' % _dir

            info += line

        info += '\n'

    #print(chardet.detect(info))
    #info = info.encode('utf-8')
    if print_mode == 'print':
        print(info)
    elif print_mode == 'write':
        with open('diff.txt', 'w') as f:
            f.write(info)
        print('write diff.txt success!')


def SynFiles(src_path, dest_path, ignore=[], syn_mode=1):
    '''
    syn_mode:
        1: 单向同步，由src_path同步至dest_path，src_path保持不变
        2: 双向同步
    '''

    diffs = CmpImageDirectory(src_path, dest_path, mode='default', ignore=ignore)
    diffs.reverse()

    dedupCopied = set()

    for diff in diffs:
        line = '%s <-> %s\n' % (diff['src'], diff['dest'])
        print(line)

        for _dir in diff['dest_miss']['dir_list']:
            if diff['src'] + _dir in dedupCopied:
                continue
            line += '    [COPYING DIR]: %s\n' % _dir
            print(line)
            shutil.copytree(diff['src'] + _dir, diff['dest'] + _dir)
            dedupCopied.add(diff['src']+_dir)
        for _file in diff['dest_miss']['file_list']:
            if diff['src'] + _file in dedupCopied:
                continue
            line += '    [COPYING FILE]: %s\n' % _file
            print(line)
            shutil.copyfile(diff['src'] + _file, diff['dest'] + _file)
            dedupCopied.add(diff['src'] + _file)



if __name__ == '__main__':
    print(__file__)
    pass
    #ignore_dirs = ['E:/Images/Web/', 'E:/Images/Present/']
    #diffs = cmp_img_dir('E:/Images', 'F:/Images', ignore=ignore_dirs)
    #printDiffs(diffs, print_mode='write')

    #ignore_dirs = ['E:/Images/Web/', 'E:/Images/Present/']
    #syn_files('E:/Images', 'F:/Images', ignore=ignore_dirs)

    #shutil.copytree('E:/Images/History/{2022.11.06}_北京马拉松', 'F:/Images/History/{2022.11.06}_北京马拉松')

