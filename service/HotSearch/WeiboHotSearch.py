# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys

sys.argv.append(os.getcwd())
sys.path.append(os.getcwd() + '/../../')

import time
import requests
import simplejson as json

def download_html(url, cookies_dir="./"):
    html = ''
    cookie_file = cookies_dir + "weibo.com.cookie"
    weibo_cookie = ""

    if os.path.exists(cookie_file):
        with open(cookie_file, "r") as fr:
            weibo_cookie = fr.read()
    else:
        weibo_cookie = \
"SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WW8HvYJSXpYZTGFsUaymCKa; \
UOR=www.baidu.com,weibo.com,www.baidu.com; \
SINAGLOBAL=48828572436.998566.1678416316360; \
SUB=_2AkMTTaGdf8NxqwJRmPodzmzkaYx1wwvEieKlEVBGJRMxHRl-yT9vqnFYtRB6OM2PcgXSfJWpJIcDbmKZ0R12jkuaa1N1; \
_s_tentry=www.baidu.com; \
Apache=2406137559614.796.1679297740246; ULV=1679297740258:2:2:1:2406137559614.796.1679297740246:1678416316362"

    req = requests.get(url)
    headers = {
        "cookie": weibo_cookie
    }

    for i in range(3):
        try:
            req = requests.get(url, headers=headers)
            new_cookie = req.headers.get("Set-Cookie", "")
            if not new_cookie:
                new_cookie = req.headers.get("set-cookie", "")
            if new_cookie and cookies_dir != "./":
                with open(cookie_file, "w") as fw:
                    fw.write(new_cookie)
            html = req.text

            if html:
                break
        except Exception as e:
            print('Exception e=%s' % str(e))
            time.sleep(10)

    return html


def parse_html(html, url=""):
    if url == "https://weibo.com/ajax/statuses/hot_band":
        d = json.loads(html)
        return d
    if url == "https://s.weibo.com/top/summary?cate=socialevent":
        return {}

    return {}

def parse_json_dict(json_dict):
    data_list = []

    data = json_dict.get("data", {})
    if not data:
        print("ERROR: json dict -> data empty!")
        return
    if not isinstance(data, dict):
        print("ERROR: data is not dict!")
        return
    cards = data.get("cards", [])
    if not cards:
        print("ERROR: data -> cards empty!")
        return
    if not isinstance(cards, list):
        print("ERROR: cards is not list!")
        return
    card = cards[0]
    if not isinstance(card, dict):
        print("ERROR: card is not dict!")
        return
    content = card.get("content", [])
    if not content:
        print("ERROR: card -> content empty!")
        return
    if not isinstance(content, list):
        print("ERROR: content is not list!")
        return
    for item in content:
        print(item.get("query", ""))
        print(item.get("word", ""))
        print(item.get("desc", ""))
        print(item.get("img", ""))
        print(item.get("hotScore", ""))


def parse_html(html):
    d = json.loads(html)
    return d


if __name__ == '__main__':
    print(__file__)
    print(os.getcwd() + '/../../')

    #html = download_html("https://weibo.com/ajax/statuses/hot_band")
    #print(html)
    #json_dict = parse_html(html)
    #print(json_dict)
    #parse_json_dict(json_dict)

    html = download_html("https://s.weibo.com/top/summary?cate=socialevent")
    print(html)