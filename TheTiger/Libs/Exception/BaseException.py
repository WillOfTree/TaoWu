"""
    错误响应信息处理函数，通过raise抛出
"""
import json

from flask import request

from werkzeug.exceptions import HTTPException


class Base(HTTPException):
    code = 500
    msg = "sorry"
    error_code = 999
    headers = ""

    def __init__(self, 
            msg:str=None, code:int=None, 
            error_code:int=None, headers:str=None
            ):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        if headers:
            self.header = headers

        super(BaseException, self).__init__(msg, None)


    def get_body(self, environ=None):
        """
            返回信息，json序列化重写
        """
        body = dict(
            msg = self.msg,
            error_code = self.error_code,
            request = request.method + " " + self.get_url_no_param()
        )
        return json.dumps(body)


    def get_headers(self):
        """
            设置返回信息的 响应头
        """
        return [("Content-Type", "appliction/json")]


    @staticmethod
    def get_url_no_param():
        """
            获取请求方法的请求路径
        """
        full_path = str(request.full_path)
        main_path = full_path.split("?")
        return main_path[0]


class APIBase(BaseException):
    code = 500
    msg = "sorry"
    error_code = 999
    headers = ""

    def get_headers(self):
        """
            设置返回信息的 响应头
        """
        return [("Content-Type", "appliction/json")]


class HomeBase(BaseException):
    def get_headers(self):
        return [("Content-Type", "appliction/html")]