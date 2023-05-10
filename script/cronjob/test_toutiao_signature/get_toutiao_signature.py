# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import time
import math
import hashlib

def getHoney():
    i = math.floor(time.time())
    e = str('%X' % i)
    md5 = hashlib.md5()
    md5.update(str(i).encode('utf-8'))
    t = str(md5.hexdigest()).upper()
    if 8 != len(e):
        return {
            'as':"479BB4B7254C150",
            'cp':"7E0AC8874BB0985"
        }
    o = t[0:5]
    n = t[-5:]
    a = ''
    r = ''
    for i in range(5):
        a += o[i] + e[i]
        r += e[i + 3] + n[i]
    return {
        'as':"A1" + a + e[-3:],
        'cp':e[0:3] + r + "E1"
    }


def get_signature():

    url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_p"
    sign = os.popen('D:/code/SDK/nodejs/node.exe  D:/code/PythonProjects/script/cronjob/get_sign.js {url}'.format(url='"'+url+'"')).read()
    return sign


if __name__ == '__main__':
    sign = get_signature()
    print("sign:", sign)
