# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys

sys.argv.append(os.getcwd())
sys.path.append(os.getcwd() + '/../../')

import time
import requests
import simplejson as json

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
    d = json.loads(html)
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

    html = download_html("https://weibo.com/ajax/statuses/hot_band")
    print(html)
    json_dict = parse_html(html)
    print(json_dict)
    #parse_json_dict(json_dict)