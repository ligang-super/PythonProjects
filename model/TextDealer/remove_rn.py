# -*- coding:utf-8 -*-
# __author__='ligang'


import json
import os
import requests
import json
import chardet

import common.common_string


def remove_r_n(fpath):
    f = open(fpath, 'rb')

    data = f.read()
    text = data.decode('utf-8')
    #print(text)

    last_ch = ""
    s = set({'；', '!', '：', '？', '。', '！', '…'})

    new_text = ""
    for ch in text:
        if ch in ("\r", "\n"):
            if last_ch in s:
                new_text += ch
            else:
                continue
        else:
            new_text += ch
            #print(new_text)
        last_ch = ch

    print(new_text, len(new_text))

    nf = open("new_c5.txt", 'w')
    nf.write(new_text)
    nf.close()



if __name__ == '__main__':
    print("Hello", os.path.basename(__file__))

    fpath = "C:/Users/ligang33/Downloads/c5.txt"
    remove_r_n(fpath)



