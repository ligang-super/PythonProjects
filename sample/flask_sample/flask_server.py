# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys

sys.argv.append(os.getcwd())
sys.path.append(os.getcwd() + '/../../')

import time
import datetime
import numpy as np
import xml.etree.ElementTree as ET


import flask
import simplejson as json
from flask import request
import base64
import io


'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
# 创建一个服务，把当前这个python文件当做一个服务




server = flask.Flask(__name__)

@server.route('/hello', methods=['GET'])
def hello():
    # 获取通过url请求传参的数据
    print("hello")
    k = request.args.get("k")
    v = request.args.get("v")
    print("k:", k, "v:", v)
    return flask.jsonify({'k': k, 'v': v}), 200


if __name__ == '__main__':
    server.run(debug=True, port=8080, host='0.0.0.0')  # 指定端口、host设为0.0.0.0代表不管几个网卡，任何ip都可以访问


