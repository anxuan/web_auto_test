# coding:utf-8
import unittest,sys
from HTMLTestRunner_PY3 import HTMLTestRunner
import time,os
# 用例路径
case_path = os.path.join(os.getcwd(), "testcase")
print(case_path)
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
email_path = os.path.join(os.getcwd(), "common")

sys.path.append(email_path)
print(sys.path)
#report_file = os.path.join(report_path,'/report.txt/')
report_file = os.path.join(report_path,'report.txt')
if 'report.txt' in os.listdir(report_path):
    os.remove(report_file)
#report_file = "E:\\测试\\interface_test\\report\\report.txt"
print("######"+report_path)
print("*******"+report_file)
from send_mail import *
def creatsuite():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

#discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        print(test_case)
        testunit.addTests(test_case)
    return testunit
'''
now = time.strftime("%Y-%m-%d %H_%M_%S")
testfile=os.path.join(os.getcwd(),'report')
print(testfile)
filename = testfile+'\\'+now+'result.html'
fp = open(filename, 'wb+')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')

if __name__ == '__main__':
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
'''
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(creatsuite())
    send_mail(report_file)
    
