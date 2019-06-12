#coding: utf-8
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
import unittest
import smtplib
from email.mime.text import MIMEText
import time,os
def send_mail(file_new):
    mail_from='liuqiancheng0021@163.com'#邮件发送地址
    #mail_to='xupeiqing@artbloger.com'#邮件接收地址
    mail_to='liuqiancheng0021@163.com'#邮件接收地址
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='gbk')
    msg['from']=mail_from
    msg['to']=mail_to
    msg['Subject']=u"直链网F端自动化报告"
    msg['Accept-Language']='zh-CN'
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    #msg = MIMEText(content,format,'gbk')
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(mail_from,'F123456')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print("发送邮件成功")

if __name__ == '__main__':
    send_mail('E:/测试/interface_test/report/report.txt')
