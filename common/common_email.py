# -*- coding:utf-8 -*-
# __author__='LiGang'

import os
import sys

sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/../')

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class EmailServer(object):
    def __init__(self, host, user, password, sender) -> None:
        # 邮箱服务器地址
        self.host = host
        # 邮箱用户名
        self.user = user
        # 邮箱密码或授权码
        self.password = password
        # 邮件发送方邮箱地址
        self.sender = sender

        # 待发送邮件信息
        self.email_title = ""
        self.email_content = ""
        self.receivers = []
        self.attachments = []
        self.message = None

    def login_and_send(self, message):
        # 登录并发送邮件
        try:
            smtp_obj = smtplib.SMTP()
            # 连接到服务器
            smtp_obj.connect(self.host, 25)
            # 登录到服务器
            smtp_obj.login(self.user, self.password)
            # 发送
            smtp_obj.sendmail(
                self.sender, self.receivers, message.as_string())
            # 退出
            smtp_obj.quit()
            print('success')
            return True
        except smtplib.SMTPException as e:
            # 打印错误
            print('error', e)
        return False

    def set_title(self, title):
        self.email_title = title

    def set_content(self, content):
        self.email_content = content

    def add_receiver(self, receiver):
        self.receivers.append(receiver)

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

    def make_message(self):
        self.message = None



def __test_email():
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = 'ligang33baidu'
    # 授权码
    mail_pass = 'XSZEQMAAQEDQHPWJ'
    # 邮件发送方邮箱地址
    sender = 'ligang33baidu@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['ligang33@baidu.com', 'ligang33baidu@163.com']

    # 设置email信息
    # 邮件内容设置
    # message = MIMEText('content', 'plain', 'utf-8')
    message = MIMEMultipart()
    # 邮件主题
    message['Subject'] = 'title'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = 'ligang33@baidu.com; ligang33baidu@163.com'

    # 推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
    with open('D:/code/data/test/20230321_113631_entrank.html', 'rb') as fhtml:
        html_content = fhtml.read()
    # 设置html格式参数
    attached_html = MIMEText(html_content, 'html', 'utf-8')
    #attached_html['Content-Type'] = 'application/octet-stream'
    #attached_html['Content-Disposition'] = 'attachment;filename="20230321_113631_entrank.html"'

    # 添加一个txt文本附件
    with open('D:/code/data/test/新建文本文档.txt', 'r') as ftxt:
        txt_content = ftxt.read()
    # 设置txt参数
    attached_txt = MIMEText(txt_content, 'plain', 'utf-8')
    # 附件设置内容类型，方便起见，设置为二进制流
    attached_txt['Content-Type'] = 'application/octet-stream'
    # 设置附件头，添加文件名
    attached_txt['Content-Disposition'] = 'attachment;filename="abc.txt"'

    # 添加照片附件
    with open('D:/code/data/test/微信图片_20230315103151.jpg', 'rb') as fimg:
        attached_img = MIMEImage(fimg.read())
        # 与txt文件设置相似
        attached_img['Content-Type'] = 'application/octet-stream'
        attached_img['Content-Disposition'] = 'attachment;filename="1.png"'
    # 将内容附加到邮件主体中
    message.attach(attached_html)
    message.attach(attached_txt)
    message.attach(attached_img)

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        # 打印错误
        print('error', e)


def SendEmailWithDefaultConfig(to_email="", title="", content="", files=[]):
    '''
    使用默认配置，发送邮件
    params:
        to_email: 目标邮件地址
        title: 邮件主题
        content: 邮件内容
        files: 附件
    ret:
        bool 发送是否陈工
    '''

    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = 'ligang33baidu'
    # 授权码
    mail_pass = 'XSZEQMAAQEDQHPWJ'
    # 邮件发送方邮箱地址
    sender = 'ligang33baidu@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = [to_email]

    # 设置email信息
    # 邮件内容设置
    message = MIMEMultipart()
    # 邮件主题
    message['Subject'] = title
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 正文内容
    email_content = MIMEText(content, 'plain', 'utf-8')
    message.attach(email_content)

    # 推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
    with open('D:/code/data/test/20230321_113631_entrank.html', 'rb') as fhtml:
        html_content = fhtml.read()
    # 设置html格式参数
    attached_html = MIMEText(html_content, 'html', 'utf-8')
    attached_html['Content-Type'] = 'application/octet-stream'
    attached_html['Content-Disposition'] = 'attachment;filename="20230321_113631_entrank.html"'

    # 添加一个txt文本附件
    with open('D:/code/data/test/新建文本文档.txt', 'r') as ftxt:
        txt_content = ftxt.read()
    # 设置txt参数
    attached_txt = MIMEText(txt_content, 'plain', 'utf-8')
    # 附件设置内容类型，方便起见，设置为二进制流
    attached_txt['Content-Type'] = 'application/octet-stream'
    # 设置附件头，添加文件名
    attached_txt['Content-Disposition'] = 'attachment;filename="abc.txt"'

    # 添加照片附件
    with open('D:/code/data/test/微信图片_20230315103151.jpg', 'rb') as fimg:
        attached_img = MIMEImage(fimg.read())
        # 与txt文件设置相似
        attached_img['Content-Type'] = 'application/octet-stream'
        attached_img['Content-Disposition'] = 'attachment;filename="1.png"'
    # 将内容附加到邮件主体中

    message.attach(attached_html)
    message.attach(attached_txt)
    message.attach(attached_img)

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        # 打印错误
        print('error', e)


if __name__ == '__main__':
    print(__file__)
    __test_email()
