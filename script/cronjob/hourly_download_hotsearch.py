# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys

sys.argv.append(os.getcwd())
sys.path.append(os.getcwd() + '/../../')

import time
import requests
import simplejson as json
from datetime import datetime

from service.HotSearch import BaiduHotSearch
from service.HotSearch import WeiboHotSearch

BAIDU_HOT_SEARCH_URL = "https://top.baidu.com/board?tab=realtime"
BAIDU_HOT_SEARCH_DATA_DIRECTORY = "/home/ligang/data/baidu_hot_search/"
WEIBO_HOT_SEARCH_URL = "https://weibo.com/ajax/statuses/hot_band"
WEIBO_HOT_SEARCH_DATA_DIRECTORY = "/home/ligang/data/weibo_hot_search/"


def downloadBaiduHot():
    nowstr = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = BAIDU_HOT_SEARCH_DATA_DIRECTORY + nowstr + '.json'
    html = BaiduHotSearch.download_html(BAIDU_HOT_SEARCH_URL)
    json_dict = BaiduHotSearch.parse_html(html)

    with open(fname, "w") as f:
        json.dump(json_dict, f, ensure_ascii=False)

def downloadWeiboHot():
    nowstr = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = WEIBO_HOT_SEARCH_DATA_DIRECTORY + nowstr + '.json'
    html = WeiboHotSearch.download_html(WEIBO_HOT_SEARCH_URL)
    json_dict = WeiboHotSearch.parse_html(html)

    with open(fname, "w") as f:
        json.dump(json_dict, f, ensure_ascii=False)

if __name__ == '__main__':
    print(__file__)
    downloadBaiduHot()
    downloadWeiboHot()



