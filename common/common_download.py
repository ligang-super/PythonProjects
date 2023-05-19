# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys
import time
import requests


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