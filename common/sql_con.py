import pymysql,sys
sys.path.append("../")
from config import *
sql = ''
# 打开数据库连接
#version = cursor.execute("SELECT VERSION()")
#print(version)
'''
    def __init__(self,host=host,username=username,password=password,database=database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.sql = sql
        self.db = pymysql.connect(self.host,self.username,self.password,self.database)
        self.cursor = self.db.cursor()
        '''
db = pymysql.connect(host,username,password,database)
print(host,username,password,database)
cursor=db.cursor()
def exe_sql(sql):
    return cursor.execute(sql)
    db.close()

def fetchone(sql):
    print(sql)
    cursor.execute(sql)
    return cursor.fetchone()
    print(cursor.fetchone())
    db.commit()
    cursor.close()
    db.close()
    
def fetchall(sql):
    cursor.execute(sql)
    return cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
        
if __name__=="__main__":
    #sql = "select * from t_shopping_cart where member_id = (SELECT id from t_member where member_id = '15500000000') and is_buy = 0"
    sql = "select * from t_shopping_cart t"
    print((sql))
    res = cursor.execute(sql)
    print(res)
    version = cursor.execute("SELECT VERSION()")
    print(version)
