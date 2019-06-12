import os
def new_log(testlog):
   lists = os.listdir(testlog)
   lists.sort(key=lambda fn: os.path.getmtime(testlog + "\\" + fn))
   print(('最新测试结果' + lists[-1]))
   file_new = os.path.join(testlog,lists[-1])
   print(file_new)
   return file_new
