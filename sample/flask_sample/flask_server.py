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
from config.config_logging import setup_logger
from ggsdk.mysql import common_pymysql

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
# 创建一个服务，把当前这个python文件当做一个服务


server = flask.Flask(__name__)

life_dbw = None

@server.route('/hello1', methods=['GET'])
def hello1():
    # 获取通过url请求传参的数据
    print("hello1")
    k = request.args.get("k")
    v = request.args.get("v")
    print("k:", k, "v:", v)
    return flask.jsonify({'k': k, 'v': v}), 200


@server.route('/hello2', methods=['GET'])
def hello2():
    # 获取通过url请求传参的数据
    print("hello1")
    k = request.args.get("k")
    v = request.args.get("v")
    print("k:", k, "v:", v)

    r = {'code': '200', 'k': k, 'v': v}  # 返回数据

    return json.dumps(r, ensure_ascii=False), 200


def init_life_dbw():
    mysql_logger = setup_logger("test_mysql", "../../model/Test/log/", "mysqldb")

    dbw = common_pymysql.MysqlClientPool(dbuser='root',
                                         dbpass='mysql_123456',
                                         pool_size=10,
                                         cls_name=common_pymysql.MysqlConnection,
                                         host='180.76.69.162',
                                         port=8306,
                                         dbname='life',
                                         enc='utf8mb4',
                                         logger=mysql_logger)
    if not dbw:
        print("dbw is none")
        exit(-1)

    r1 = dbw.get_data_by_id(table='sai_ke_si_info', idx=1)
    print(r1)

    rdata = dbw.get_data(table='sai_ke_si_info')
    print(rdata)

    '''
    ret = dbw.insert_data(table='test_table', val_dict={'uid': 100}, has_crtime=True)
    print(ret)
    r1 = dbw.get_data_by_id(table='test_table', idx=1)
    print(r1)

    r2 = dbw.get_data(table='test_table', conditions=['uid > %d'], condvalues=[5])
    print(r2)

    '''
    return dbw

life_dbw = init_life_dbw()

if __name__ == '__main__':
    server.run(debug=True, port=8080, host='0.0.0.0')  # 指定端口、host设为0.0.0.0代表不管几个网卡，任何ip都可以访问
