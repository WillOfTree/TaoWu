""" 对某些请求进行处理的方法 """
from System import Flask_app


###------------
# 处理开始请求
@Flask_app.before_request
def request_start():
    print("befor_request")