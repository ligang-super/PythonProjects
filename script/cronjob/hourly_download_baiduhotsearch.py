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

from service.HotSearch import baiduHotSearch

BAIDU_HOT_SEARCH_URL = "https://top.baidu.com/board?tab=realtime"

if __name__ == '__main__':
    print(__file__)
    nowstr = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = os.getcwd() + '/../../data/baidu_hot_search/' + nowstr + '.json'
    html = baiduHotSearch.download_html(BAIDU_HOT_SEARCH_URL)
    json_dict = baiduHotSearch.parse_html(html)

    with open(fname, "w") as f:
        json.dump(json_dict, f, ensure_ascii=False)
