# -*-coding:utf-8-*-
#
# base_headler
#
# 公共处理headler
# --------------
#
# 用于初始化参数，配置默认返回值

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    @property
    def db(self): # 设置mysql属性
        return self.application.db

    @property
    def redis(self):  # 设置redis属性
        return self.application.redis

    def prepare(self):
        pass

    def write_error(self):
        pass

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        # self.set_header('Access-Control-Max-Age', 1000)
        # self.set_header('Content-type', 'application/json')
        # self.set_header('Access-Control-Allow-Methods', 'POST, GET, DELETE, PUT, PATCH, OPTIONS')
        # self.set_header('Access-Control-Allow-Headers',
        #                 'Content-Type, token, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
        pass

    def initialize(self):
        pass

    def on_finish(self):
        pass

    def options(self):
        pass