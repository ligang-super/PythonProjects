import sys
import os
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


@server.route('/tf_object_detection', methods=['GET'])
def tf_object_detection():
    # 获取通过url请求传参的数据
    print(request.headers.get("content_type"))
    jsondata = request.get_json()
    print(jsondata)
    if jsondata:
        print("jsondata len=%d" % len(jsondata))
    else:
        print("jsondata is none")

    data = jsondata

    username = data.get('name', '')

    r = {'code': '200', 'result': 'success!'}  # 返回数据

    return json.dumps(r, ensure_ascii=False)  # 将字典转换为json串, json是字符串


if __name__ == '__main__':
    server.run(debug=True, port=80, host='0.0.0.0')  # 指定端口、host设为0.0.0.0代表不管几个网卡，任何ip都可以访问



