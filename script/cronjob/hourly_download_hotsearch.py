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

WEIBO_SOCIAL_EVENT_URL = "https://s.weibo.com/top/summary?cate=socialevent"
WEIBO_ENT_RANK_URL = "https://s.weibo.com/top/summary?cate=entrank"
WEIBO_SPORT_URL = "https://s.weibo.com/top/summary?cate=sport"
WEIBO_GAME_URL = "https://s.weibo.com/top/summary?cate=game"

WEIBO_HOT_SEARCH_DATA_DIRECTORY = "/home/ligang/data/weibo_hot_search/"

COOKIES_DIRECTORY = "/home/ligang/data/cookies/"


def downloadBaiduHot():
    nowstr = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname_hotsearch = BAIDU_HOT_SEARCH_DATA_DIRECTORY + nowstr + '.json'
    html_hotsearch = BaiduHotSearch.download_html(BAIDU_HOT_SEARCH_URL)
    json_dict = BaiduHotSearch.parse_html(html_hotsearch)

    with open(fname_hotsearch, "w") as f:
        json.dump(json_dict, f, ensure_ascii=False)

def downloadWeiboHot():
    nowstr = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 下载热搜榜
    fname_hotsearch = WEIBO_HOT_SEARCH_DATA_DIRECTORY + nowstr + '.json'
    html_hotsearch = WeiboHotSearch.download_html(WEIBO_HOT_SEARCH_URL)
    json_dict = WeiboHotSearch.parse_html(html_hotsearch)

    with open(fname_hotsearch, "w") as f:
        json.dump(json_dict, f, ensure_ascii=False)

    # 下载要闻榜、文娱榜、体育榜、游戏榜
    url_dict = {
        "socialevent": WEIBO_SOCIAL_EVENT_URL,
        "entrank": WEIBO_ENT_RANK_URL,
        "sport": WEIBO_SPORT_URL,
        "game": WEIBO_GAME_URL
    }

    for category, down_url in url_dict.items():
        fname = WEIBO_HOT_SEARCH_DATA_DIRECTORY + nowstr + "_" + category + '.html'
        html = WeiboHotSearch.download_html(down_url, cookies_dir=COOKIES_DIRECTORY)

        with open(fname, "w") as f:
            f.write(html)



if __name__ == '__main__':
    print(__file__)
    downloadBaiduHot()
    downloadWeiboHot()



