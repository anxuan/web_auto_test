#coding: utf-8
import os,sys
sys.path.append("../")
from config import *
#report_path=os.path.join(os.path.split(os.getcwd())[0],"report")
class report:
    def __init__(self,content):
        self.report_file=report_file
        self.content=content
    def write_file(self):
        #path = os.path.join(report_path,self.report_file)
        with open(report_file,"a+") as f:
            f.write(self.content+'<br/>')
            
        

if __name__ == '__main__':
    tt = report('test12345645').write_file()
