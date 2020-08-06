#!/usr/bin/env python
# -*- coding:utf-8 -*-
# fileName: run_email.py
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib


# 定义发邮件
def send_mail(file_path):

    f = open(file_path, 'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.qq.com'
    # 设置登录邮箱的账号和授权密码
    user = 'XXX@qq.com'
    password = "XXX"
    sender = 'XXX@qq.com'
    # 可添加多个收件人的邮箱
    receives = ['XXX@qq.com']
    # 构造邮件对象
    msg = MIMEMultipart('mixed')
    # 定义邮件的标题
    subject = '接口自动化测试报告'
    # HTML邮件正文，定义成字典
    msg['Subject'] = Header(subject, "utf-8")
    msg['From'] = sender
    msg['To'] = ','.join(receives)
    # 构造文字内容
    # text_plain = MIMEText(mail_body, 'html', 'utf-8')
    text_plain = MIMEText("附件是最新的接口自动化测试报告，请查看", 'html', 'utf-8')
    msg.attach(text_plain)
    # 构造附件
    text_attr = MIMEText(mail_body, 'base64', 'utf-8')
    text_attr["Content-Type"] = 'application/octet-stream'
    text_attr['Content-Disposition'] = 'attachment; filename = "test.html"'
    msg.attach(text_attr)

    # 邮箱设置时勾选了SSL加密连接，进行防垃圾邮件，SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 向服务器返回确认结果
    smtp.ehlo(smtpserver)
    # 登录邮箱的账号和授权密码
    smtp.login(user, password)

    print("开始发送邮件...")
    # 开始进行邮件的发送，msg表示已定义的字典
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("已发送邮件")


if __name__ == "__main__":
    report = "../testcase/report/all_report.html"
    send_mail(report)