# -*- coding:utf-8 -*-
# __author__='LiGang'

import os
import sys
import datetime
import flask
import flask_login
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from flask_login import login_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

from config.config_logging import setup_logger
from ggsdk.mysql import common_pymysql
from model.HttpServer.web_server import mysql_lifedb
from model.HttpServer.web_server import task_saikesi, task_baiwangshan
from conf.web_server_conf import LOGIN_USERS, SERVER_SECRET_KEY


server = Flask(__name__, template_folder='../templates', static_folder='../static')
server.secret_key = SERVER_SECRET_KEY

login_manager = flask_login.LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'
login_manager.init_app(server)

# 设置静态文件缓存过期时间
server.config.send_file_max_age_default = timedelta(seconds=1)
server.register_blueprint(task_saikesi.saikesi_job)
server.register_blueprint(task_baiwangshan.baiwangshan_job)


@server.route('/login', methods=['GET', 'POST'])
def login():
    next_url = flask.request.args.get("next", "")
    print("next_url1:", next_url, flask.request.method)
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='username' id='username' placeholder='username'/>
                <input type='hidden' name='next_url' id='next_url' placeholder='next_url' value='{next_url}'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''.format(next_url=next_url)

    username = flask.request.form['username']
    next_url = flask.request.form['next_url']
    if username in LOGIN_USERS and flask.request.form['password'] == LOGIN_USERS[username]['password']:
        user = User()
        user.id = username
        flask_login.login_user(user)

        print("next_url2:", next_url)

        return flask.redirect(next_url)
    return 'Bad login'


@server.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    if username not in LOGIN_USERS:
        return

    user = User()
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in LOGIN_USERS:
        return

    user = User()
    user.id = username
    return user


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8999, debug=False)






