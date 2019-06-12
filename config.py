import os
base_url = 'http://192.168.3.214:8801/'
base_url_FPC = 'http://192.168.3.214:8803/'


#[DATABASE]
host = '192.168.3.214'
username = 'developer'
password = 'DEVops2019'
#port = 3306
database = 'zlead_f'
#[log_path]
log_path = os.path.join(os.getcwd(),"log")
print(log_path)
#[report_name]
#report_path=os.path.join(os.path.split(os.getcwd())[0],"report")
report_path=os.path.join(os.getcwd(),"report")
report_file=os.path.join(report_path,'report.txt')
print(report_file)

