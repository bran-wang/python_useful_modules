#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(content):
    sender = "onesafe@163.com"
    receiver = ["branw@vmware.com"]
    host = "smtp.163.com"
    port = 465
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = "onesafe@163.com"
    msg['To'] = "branw@vmware.com"
    msg['Subject'] = "警告：system error warning"

    try:
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.login(sender, "your password")
        smtp.sendmail(sender, receiver, msg.as_string())
    except Exception, e:
        print e


if __name__ == "__main__":
    send_email("hello, 摩托")
