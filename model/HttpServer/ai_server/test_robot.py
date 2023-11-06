import sys
import os
import flask
import simplejson as json
from flask import request, jsonify
import base64
import io
from urllib.parse import parse_qs

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
# 创建一个服务，把当前这个python文件当做一个服务

#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import binascii

import six
# pip install pycrypto
# Windows No module named Crypto.Cipher问题，https://www.jianshu.com/p/09a14a61b454

encodingAESKey = 'YeYVnnvO7yuVEUK3SHDKbd'
webhook_url = 'http://apiin.im.baidu.com/api/msg/groupmsgsend?access_token=d984778b17c253bc5c5cf470e40674a33'

'''
from Crypto.Cipher import AES


def base64_urlsafe_decode(s):
    """
    base64 解码(urlsafe兼容模式)
    :return:
    """
    # 系统的urlsafe_b64decode方法不支持补'='
    s = s.replace('-', '+').replace('_', '/') + '=' * (len(s) % 4)

    return base64.b64decode(s)


class AESCipher(object):
    """
    AES加解密类
    """

    def __init__(self, key, mode=AES.MODE_ECB, padding='PKCS7', encode='base64', **kwargs):
        """
        初始化
        :param key:
        :param mode:
        :param padding: 数据填充方式 PKCS7、ZERO
        :param encode: 数据编码方式 raw、base64、hex
        """
        self.key = key
        self.mode = mode
        self.padding = padding
        self.encode = encode
        self.kwargs = kwargs

        self.bs = AES.block_size

        self.IV = self.kwargs.get('IV', None)
        if self.IV and self.mode in (AES.MODE_ECB, AES.MODE_CTR):
            raise TypeError("ECB and CTR mode does not use IV")

    def _aes(self):
        return AES.new(self.key, self.mode, **self.kwargs)

    def encrypt(self, plaintext):
        """
        加密
        :param plaintext:
        :return: py3返回 byte string, py2返回str
        """
        # padding https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS#5_and_PKCS#7
        if self.padding == 'PKCS7':
            pad = lambda s: s + (self.bs - len(s) % self.bs) \
                            * chr(self.bs - len(s) % self.bs).encode('utf-8')
        else:
            pad = lambda s: s + (self.bs - len(s) % self.bs) \
                            * '\x00'
        # 统一为字节类型
        if isinstance(plaintext, six.text_type):
            plaintext = plaintext.encode('utf-8')

        # 注意：加密、解密需单独实例化
        raw = self._aes().encrypt(pad(plaintext))

        if self.encode == 'hex':
            return binascii.hexlify(raw)
        if self.encode == 'base64':
            return base64.b64encode(raw)
        return raw

    def decrypt(self, ciphertext):
        """
        解密
        :param ciphertext:
        :return: py3返回 byte string, py2返回str
        """
        if not ciphertext:
            return None

        if self.padding == 'PKCS7':
            if six.PY3:
                unpad = lambda s: s[0:-s[-1]]
            else:
                unpad = lambda s: s[0:-ord(s[-1])]
        else:
            unpad = lambda s: s.rstrip('\x00')

        # 统一为文本字符类型
        if isinstance(ciphertext, six.binary_type) and self.encode != 'raw':
            ciphertext = ciphertext.decode('utf-8')
        if self.encode == 'hex':
            ciphertext = binascii.unhexlify(ciphertext)
        if self.encode == 'base64':
            ciphertext = base64_urlsafe_decode(ciphertext)

        return unpad(self._aes().decrypt(ciphertext))



server = flask.Flask(__name__)


@server.route('/robot_msg', methods=['GET', 'POST'])
def robot_msg():
    # 获取通过url请求传参的数据

    # 获取POST参数echostr，Django可使用request.POST.get('echostr', None)
    # 注意：仅回调配置的时候有此参数，需要指定缺省值
    echostr = request.form.get('echostr', None)
    # 配置回调地址时应回调服务就绪，配置回调地址时会调用配置地址，需要回显才能校验通过
    if echostr:
        return echostr
    else:
        # 获取request raw body, Django可使用request.body
        msg_base64 = request.get_data()
        encrypter = AESCipher(base64_urlsafe_decode(encodingAESKey))
        # 通过AES解密后得到回调消息数据
        decrypted = encrypter.decrypt(msg_base64)
        msg_data = json.loads(decrypted)
        print(msg_data)

        send_msg()
        return ""


    print(request.method)
    print(request.headers)
    if request.method == 'GET':
        # 解析GET参数
        name = request.args.get('name')
        message = f'Hello, {name}!'
        return message

    elif request.method == 'POST':
        # 解析POST参数
        data = request.form
        print(data)

        parsed_data = data.to_dict()

        print(parsed_data)
        name = data.get('signature')
        message = f'Hello, {name}!'
        return parsed_data['echostr']

    else:
        return 'Invalid request method'

    r = {'code': '200', 'name': name, 'result': 'success!'}  # 返回数据
    return json.dumps(r, ensure_ascii=False)  # 将字典转换为json串, json是字符串
'''

def send_msg():
    import requests

    url = webhook_url
    payload = {
    "message":{
        "header":{
            "toid":[8916636]
        },
        "body":[
            {
                "content":"大家好，这是来自机器人的消息\n",
                "type":"TEXT"
            },
            {
                "atuserids":["ligang33"],
                "atall":False,
                "type":"AT"
            }
        ]
    }
}

    response = requests.post(url, json=payload)

    print(response.status_code)
    print(response.text)



if __name__ == '__main__':
    #server.run(debug=True, port=8123, host='0.0.0.0')  # 指定端口、host设为0.0.0.0代表不管几个网卡，任何ip都可以访问
    send_msg()
