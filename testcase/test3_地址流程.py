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
from md5parse import *
file_name="添加地址.xlsx"
url_login = base_url+'zlead/member/login'
url_query = base_url+'zlead/memaddr/getAllAgentAddress'
url_add = base_url + 'zlead/memaddr/addOrUpdateMemberAddress'
url_del = base_url+'zlead/memaddr/deleteMemberAddress'
mylogger = Logger(__name__).getlog()
#mylogger.info("本次接口测试请求地址为："+str(url)+"\n")
class test_login:
    
    def test_添加地址(self):
        #登录
        pass_count = 0
        fail_count = 0
        seesion = requests.session()
        data = {'account':"15500000000",'password':111111}
        res = seesion.get(url=url_login,params = data)
        cookies=res.cookies
        mylogger.info("获取cookie成功，cookies="+str(cookies))
        if "登录成功" in res.json().values():
            mylogger.info("登录成功")
        else:
            mylogger.info("登录失败,失败信息为："+res.json())
            #mylogger.info("第"+str(i-2)+"条用例\""+str(self.description[i].value)+"\"开始执行")
        mylogger.info("添加地址开始")
        data_add = {'memberName':"testxu",'phone':"1311111111",'provinceName':"上海市",'cityName':"市辖区",'countyName':"黄浦区",'detailAddress':"泛太平洋大厦",'isDefault':1,'type':1}
        mylogger.info("添加地址请求数据:"+str(data_add))

        p=seesion.post(url=url_add,data=data_add,cookies=cookies)
        mylogger.info("添加地址返回数据:"+str(p.text))
        if "地址添加成功！" in p.json().values():
            mylogger.info("添加地址结束，测试结果为：成功")

        else:
            mylogger.info("添加地址结束，测试结果为：失败")
                
        #if "地址添加成功！" in p.json().values():
         #   #self.sheet[('L'+str(i+1))]="成功"
          #  self.data.save(self.real_path)
           # mylogger.info("添加地址结束，结果为：成功")
            #pass_count.append(i)
                
        #else:
                #self.sheet[('L'+str(i+1))]="失败"
         #   self.data.save(self.real_path)
          #  mylogger.info("添加地址结束，结果为：失败")
                #fail_count.append(i)
                #print(fail_count)

        mylogger.info("查询地址开始")
        data_query = {}
        mylogger.info("请求数据为："+url_query)
        t = seesion.post(url = url_query,data = data_query,cookies = cookies)
        mylogger.info("查询地址返回数据为："+str(t.json()))
        if "地址列表" in t.json().values():
            mylogger.info("查询地址结束，测试结果为：成功")

        else:
            mylogger.info("查询地址结束，测试结果为：失败")
        print((t.json()['data'])['0'][-1]['id'])
        addressId = (t.json()['data'])['0'][-1]['id']
        #print(t.json()[data])
        mylogger.info("更新地址开始")
        data_update = {'addressId':addressId,'memberName':"testxu1",'phone':"1311111111",'provinceName':"上海市",'cityName':"市辖区",'countyName':"黄浦区",'detailAddress':"泛太平洋大厦",'isDefault':1,'type':2}
        mylogger.info("更新地址请求数据:"+str(data_update))
        tt = seesion.post(url = url_add,data = data_update,cookies = cookies)
        mylogger.info("更新地址返回数据为："+str(tt.text))
        if "地址修改成功！" in tt.json().values():
            mylogger.info("更新地址结束，测试结果为：成功")

        else:
            mylogger.info("更新地址结束，测试结果为：失败")
            fail_count = 1

        mylogger.info("删除地址开始")
        data_del = {'addressId':addressId}
        ttt = seesion.post(url = url_del,data = data_del,cookies = cookies)
        mylogger.info("删除地址返回数据："+str(ttt.json()))
        if "地址删除成功！" in ttt.json().values():
            mylogger.info("删除地址结束，测试结果为：成功")
            pass_count=1
            fail_count = 0

        else:
            mylogger.info("删除地址结束，测试结果为：失败")
            fail_count = 1
                    
        content = ('''<tr><td>登录、添加、查询、修改、删除地址流程</td><td>'''+str(pass_count+fail_count)+'''</td><td>'''+str(pass_count)+'''</td><td>'''+str(fail_count)+'''</td></tr>''')
        mylogger.info('''登录、添加、查询、修改、删除地址流程测试结果:用例总数'''+str(pass_count+fail_count)+"其中通过用例"+str(pass_count)+"条，失败用例"+str(fail_count)+'条')
        print(content)
        report(content).write_file()

#if __name__=='__main__':
test_login().test_添加地址()
