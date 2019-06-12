import requests,json,unittest,os,sys
import decimal
from openpyxl import load_workbook
#path_data=os.path.join(os.path.split(os.getcwd())[0],"testdata")
path_data=os.path.join(os.getcwd(),"testdata")
path_report=os.path.join(os.getcwd(),"common")
#path1=os.path.join(os.path.split(os.getcwd())[0],"common")
sys.path.append("../")
sys.path.append(path_report)
#from exclepase import *
from config import *
from report_write import *
from logger import *
from sql_con import *
file_name="删除购物车.xlsx"
url_login = base_url+'zlead/member/login'
url_query = base_url+'/zlead/shopcart/shoppingCartGoods'
url_add = base_url+'/zlead/shopcart/addShoppingCart'
url = base_url+'/zlead/shopcart/deleteShoppingCart'
mylogger = Logger(__name__).getlog()
mylogger.info("本次接口测试请求地址为："+str(url)+"\n")
class test_login:
    def __init__(self,file_name=file_name,Sheet_name='test'):
        self.name=file_name
        self.Sheet_name = Sheet_name
        self.real_path=os.path.join(path_data,self.name)
        self.data = load_workbook(self.real_path)        
        self.sheet = self.data[self.Sheet_name]
    
    def test_删除购物车(self):
        #登录
        pass_count = 0
        fail_count = 0

        mylogger.info("开始登录")
        seesion = requests.session()
        data = {'account':str(self.sheet["B2"].value),'password':str(self.sheet["C2"].value)}
        print(data)
        mylogger.info("请求数据信息为："+str(data))
        res = seesion.get(url=url_login,params = data)
        mylogger.info("返回数据信息为："+str(res.json()))
        cookies=res.cookies
        if "登录成功" in res.json().values():
            mylogger.info("登录成功")
        else:
            mylogger.info("登录失败,失败信息为："+res.json())
        
        mylogger.info("加入购物车开始")
        print(str(self.sheet["D2"].value))
        data1 = {'goodsId':str(self.sheet["D2"].value),'count':1,'buyType':0}
        p1=seesion.post(url = url_add,data = data1,cookies = cookies)
        print(p1.json())
        if "添加购物车成功！" in p1.json().values():
            mylogger.info("添加购物车成功")
        else:
            mylogger.info("添加购物车失败")
        

        mylogger.info("查询购物车开始")
        tt=seesion.get(url_query)
        mylogger.info("返回数据:"+str(tt.json()))
        print((tt.json()["data"])[0]['goodsList'][0]['id'])
        
        cartIds = (tt.json()["data"])[0]['goodsList'][0]['id']
        if "返回购物车信息!" in tt.json().values():
            mylogger.info("查询购物车成功")
        else:
            mylogger.info("查询购物车失败")
        data2 = {'cartIds':cartIds}
        mylogger.info("删除购物车开始")
        p2 = seesion.get(url=url,params = data2)
        mylogger.info("返回数据信息为："+str(p2.json()))
        if "删除购物车成功" in p2.json().values():
            mylogger.info("删除购物车开始")
            pass_count=+1
        else:
            mylogger.info("删除购物车失败")
            fail_count=+1

        content = ('''<tr><td>登录、加入、查询、删除购物车</td><td>'''+str(pass_count+fail_count)+'''</td><td>'''+str(pass_count)+'''</td><td>'''+str(fail_count)+'''</td></tr>''')
        mylogger.info("删除购物车接口测试结果:用例总数"+str(pass_count+fail_count)+"条，其中通过用例"+str(pass_count)+"条，失败用例"+str(fail_count)+'条')
        #print(content)
        report(content).write_file()            
#if __name__=='__main__':
test_login().test_删除购物车()
