"""这是基础的Handler类，所有的HTTP handler都要继承BaseHandler

BaseHandler主要设置了mysql的参数，redis参数，还有各种Http冬青球的方法
"""

import json

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    """ 基础 Handler """

    #/-----------
    # 参数配置
    #/-----------
    #   self.db: 设置mysql属性
    #   self.redis: 设置redis属性
    #   self.HTTP_error: http向相应码
    #---------------------------
    HTTP_error = 406

    @property
    def db(self)->any: 
        return self.application.db

    @property
    def redis(self)->any:  
        return self.application.redis


    #/---------------
    # 请求方法
    #/---------------
    #   Function initialize(): 在prepare()方法之前会经历的方法
    #   Function prepare(): 调用具体的方法前调用
    #   Function write_error(): 错误信息
    #   Function set_default_headers(): 设置默认请求头
    #   Function options(): 跨域请求调用的方法
    #   Function on_finish(): 结束请求
    #   self.flush() :刷新 将缓冲区数据输出
    #   self.finish() :完成 输出缓冲区，中断请求
    #   
    def initialize(self):
        # 验证json变量参数
        if self.request.headers.get("content-type").endswith("application/json"):
            try:
                self.json_obj = json.loads(self.request.body)
            except:
                self.json_obj = None
        else:
            self.json_obj = None

    def set_default_headers(self)->None:
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        # self.set_header('Access-Control-Max-Age', 1000)
        # self.set_header('Content-type', 'application/json')
        # self.set_header('Access-Control-Allow-Methods', 'POST, GET, DELETE, PUT, PATCH, OPTIONS')
        # self.set_header('Access-Control-Allow-Headers',
        #                 'Content-Type, token, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
        

    #/-------------
    # 自定义函数
    #/-------------
    #   Function return_error(): 返回错误码，并停止信息
    #
    def send_error(self, info:str)->None:
        self.write(info)
        self.set_status(self.HTTP_error)
        self.finish()