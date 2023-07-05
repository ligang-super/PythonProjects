# -*- coding:utf-8 -*-
# __author__='LiGang'
import os
import sys
import datetime
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify

from config.config_logging import setup_logger
from ggsdk.mysql import common_pymysql
from model.HttpServer.web_server import mysql_lifedb
from model.HttpServer.web_server import task_saikesi, task_baiwangshan


server = Flask(__name__, template_folder='../templates', static_folder='../static')
# 设置静态文件缓存过期时间
server.config.send_file_max_age_default = timedelta(seconds=1)

server.register_blueprint(task_saikesi.saikesi_job)
server.register_blueprint(task_baiwangshan.baiwangshan_job)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8999, debug=False)
