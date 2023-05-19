# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys
import time
import requests
import simplejson as json
from common.common_download import download_html

def download_html(url):
    html = ''
    for i in range(3):
        try:
            req = requests.get(url)
            html = req.text
            if html:
                break
        except Exception as e:
            print('Exception e=%s' % str(e))
            time.sleep(10)

    return html


def parse_html(html):
    sdata_begin = html.find("<!--s-data:{")
    if sdata_begin < 0:
        print("ERROR: can not find \"<!--s-data:{\"")
        return

    sdata_begin += len("<!--s-data:")
    sdata_end = html.find("-->", sdata_begin)
    if sdata_end < 0:
        print("ERROR: can not find \"-->\"")
        return
    sdata = html[sdata_begin:sdata_end]
    d = json.loads(sdata)
    return d

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





if __name__ == '__main__':
    print(__file__)
    print(os.getcwd() + '/../../')

    #html = download_html("https://top.baidu.com/board?tab=realtime")
    #print(html)
    #json_dict = parse_html(html)
    #parse_json_dict(json_dict)