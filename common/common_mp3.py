# -*- coding:utf-8 -*-
# __author__='LiGang'

import os
import sys

sys.path.append(os.getcwd() + '/../')

import time
import eyed3
from collections import defaultdict
from operator import itemgetter
from common.common_file import getAllSubs

sys.argv.append(os.getcwd())

def changeMp3Tag(dirpath=""):
    if not dirpath:
        print("invalid directory: %s" % dirpath)
        return
    dirpath = dirpath.replace("\\", "/")

    if dirpath[-1] == "/":
        pass
    else:
        dirpath = dirpath + "/"

    n = len(dirpath)
    dirname = dirpath[0:n-1]
    pos = dirname.rfind("/")
    if pos == -1:
        pass
    else:
        dirname = dirname[pos+1:]

    dirname = dirname.replace("《", "")
    dirname = dirname.replace("》", "")

    pos = dirname.rfind('-')

    if pos >= 0:
        book_name = dirname[0:pos]
        book_author = dirname[pos+1:]
    else:
        book_name = dirname
        book_author = ''

    print("dirname=%s" % dirname)

    print("reading directory: %s" % dirpath)

    fileList = os.listdir(dirpath)

    for fname in fileList:
        audiofile = eyed3.load(dirpath + fname)
        print("dealing %s" % fname)
        audiofile.tag.artist = u"LiGang"  # 参与创作的艺术家
        audiofile.tag.album = book_name  # 唱片集
        audiofile.tag.album_artist = book_author  # 唱片艺术家
        #audiofile.info.time_secs  # 时长
        #audiofile.info.size_bytes # 大小


        new_title = fname
        new_title = new_title.replace(".mp3", "")

        audiofile.tag.title = new_title  # 标题
        # audiofile.tag.track_num = 4  # 音轨编号，专辑内歌曲编号："#"
        audiofile.tag.save()

def getReadingTimeInterval(dirpath=""):
    _dirs, _files = getAllSubs(dirpath)

    d = {}
    for file in _files:
        # print(file)
        if "《" not in file or "》" not in file:
            continue

        pos1 = file.find('《')
        pos2 = file.find('》')

        pos1 += len('《')

        book_name = file[pos1:pos2]

        statinfo = os.stat(file)
        t = time.localtime(statinfo.st_ctime)

        # t.tm_year
        # t.tm_mon
        # t.tm_mday
        day = '%s-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)

        if book_name not in d:
            d[book_name] = {
                'begin': '9999-99-99',
                'end': '0000-00-00'
            }

        if day < d[book_name]['begin']:
            d[book_name]['begin'] = day

        if day > d[book_name]['end']:
            d[book_name]['end'] = day

    #print(d)
    l = []
    for k, v in d.items():
        v['book'] = k
        l.append(v)

    l.sort(key=itemgetter('end'), reverse=True)

    print("---统计所读的开始和结束时间---")
    print('总阅读 %d 本书' % len(l))
    for item in l:
        print('%s： %s ———— %s' % (item['book'], item['begin'], item['end']))


def getRecordTime(path='', mode='day', ignore_dir=[]):
    '''
    mode: day, month, year
    '''

    _dirs, _files = getAllSubs(path)

    d = defaultdict(int)

    for file in _files:
        need_ignore = False
        for _dir in ignore_dir:
            if file.startswith(_dir):
                need_ignore = True
        if need_ignore:
            continue

        #print(file)
        statinfo = os.stat(file)
        #statinfo.st_ctime()
        t = time.localtime(statinfo.st_ctime)

        #t.tm_year
        #t.tm_mon
        #t.tm_mday
        if mode =='day':
            skey = '%s-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)
        elif mode =='month':
            skey = '%s-%02d' % (t.tm_year, t.tm_mon)
        elif mode == 'year':
            skey = '%s' % t.tm_year
        else:
            skey = '%s-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)


        audiofile = eyed3.load(file)
        d[skey] += audiofile.info.time_secs

    l = []
    for k, v in d.items():
        l.append(
            {
                'time': k,
                'total_seconds': int(v),
                'hour': int(v/3600),
                'minute': int((v % 3600) / 60),
                'second': int(v % 60),
            }
        )

    l.sort(key=itemgetter('time'))

    print("---Count reading time by %s---" % mode)
    for i in l:
        print('%s: %d:%d:%d' % (i['time'], i['hour'], i['minute'], i['second']))