# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys
import time
import requests
import simplejson as json
from datetime import datetime

from service.HotSearch import BaiduHotSearch
from service.HotSearch import WeiboHotSearch
from service.HotSearch import ToutiaoHotSearch

BAIDU_HOT_SEARCH_URL = "https://top.baidu.com/board?tab=realtime"
BAIDU_HOT_SEARCH_DATA_DIRECTORY = "/data/baidu_hot_search/"

WEIBO_HOT_SEARCH_URL = "https://weibo.com/ajax/statuses/hot_band"
WEIBO_SOCIAL_REALTIME_HOT = "https://s.weibo.com/top/summary?cate=realtimehot"
WEIBO_SOCIAL_EVENT_URL = "https://s.weibo.com/top/summary?cate=socialevent"
WEIBO_ENT_RANK_URL = "https://s.weibo.com/top/summary?cate=entrank"
WEIBO_SPORT_URL = "https://s.weibo.com/top/summary?cate=sport"
WEIBO_GAME_URL = "https://s.weibo.com/top/summary?cate=game"
WEIBO_HOT_SEARCH_DATA_DIRECTORY = "/data/weibo_hot_search/"

TOUTIAO_HOT_SEARCH_URL = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc"
TOUTIAO_HOT_SEARCH_DATA_DIRECTORY = "/data/toutiao_hot_search/"
TOUTIAO_SIGNATURE = "_02B4Z6wo009015b7RkgAAIDCSI0e79IY2vuW30LAAIHvJGeSvGbSiBho27a0e3OS1.iRv7io91dIgRlGvD0HN8eBQI-2BIzRhpX-cpEVId78lVRAy1r76yhWI9O4oEohNdImV57S7WlqYKOkb3"

COOKIES_DIRECTORY = "/data/cookies/"


def downloadBaiduHot():
    nowstr = datetime.now().strftime("%Y%m%d_%H")
    fname_hotsearch = BAIDU_HOT_SEARCH_DATA_DIRECTORY + nowstr + '.json'
    if not os.path.exists(fname_hotsearch):
        html_hotsearch = BaiduHotSearch.download_html(BAIDU_HOT_SEARCH_URL)
        json_dict = BaiduHotSearch.parse_html(html_hotsearch)

        with open(fname_hotsearch, "w") as f:
            json.dump(json_dict, f, ensure_ascii=False)
    else:
        print(fname_hotsearch, "already exists")

def downloadWeiboHot():
    nowstr = datetime.now().strftime("%Y%m%d_%H")

    # 下载热搜榜
    fname_hotsearch = WEIBO_HOT_SEARCH_DATA_DIRECTORY + nowstr + '.json'

    if not os.path.exists(fname_hotsearch):
        html_hotsearch = WeiboHotSearch.download_html(WEIBO_HOT_SEARCH_URL)
        json_dict = WeiboHotSearch.parse_html(html_hotsearch)

        with open(fname_hotsearch, "w") as f:
            json.dump(json_dict, f, ensure_ascii=False)
    else:
        print(fname_hotsearch, "already exists")

    # 下载要闻榜、文娱榜、体育榜、游戏榜
    url_dict = {
        "realtimeho": WEIBO_SOCIAL_REALTIME_HOT,
        "socialevent": WEIBO_SOCIAL_EVENT_URL,
        "entrank": WEIBO_ENT_RANK_URL,
        "sport": WEIBO_SPORT_URL,
        "game": WEIBO_GAME_URL
    }

    for category, down_url in url_dict.items():
        fname = WEIBO_HOT_SEARCH_DATA_DIRECTORY + nowstr + "_" + category + '.html'

        if not os.path.exists(fname):
            html = WeiboHotSearch.download_html(down_url, cookies_dir=COOKIES_DIRECTORY)

            with open(fname, "w") as f:
                f.write(html)
        else:
            print(fname, "already exists")


def downloadToutiaoHot():
    nowstr = datetime.now().strftime("%Y%m%d_%H")

    # 下载热搜榜
    fname_hotsearch = TOUTIAO_HOT_SEARCH_DATA_DIRECTORY + nowstr + '.json'

    if not os.path.exists(fname_hotsearch):
        download_url = "%s&_signature=%s" % (TOUTIAO_HOT_SEARCH_URL, TOUTIAO_SIGNATURE)
        html_hotsearch = ToutiaoHotSearch.download_html(download_url)
        json_dict = ToutiaoHotSearch.parse_html(html_hotsearch)

        with open(fname_hotsearch, "w") as f:
            json.dump(json_dict, f, ensure_ascii=False)
    else:
        print(fname_hotsearch, "already exists")


if __name__ == '__main__':
    print(__file__)
    downloadBaiduHot()
    downloadWeiboHot()
    downloadToutiaoHot()


