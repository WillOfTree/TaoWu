#
# json序列化类的方法
#
# class Models(db.Model): # 数据库model
#       a=db.Colonm(...)
#       def keys(self):
#           return ['a'] # 设置需要返回的key
#       def __getitem__(self, item):
#           return getattr(self, item) # 返回key对应的值
#
from flask import Flask as _Flask
from flask_json import JSONEncode as _JSONEncode


class JSONEncode(_JSONEncode):
    def default(self, o):
        """ 序列化字符串， 实现序列化对象方法"""
        if hasattr(o, "keys") and hasattr(o, "__getitem__"):
            return dict(o)
        if isinstance(o, date): # 添加序列化时间的方法
            return o.strftime("%Y-%m-%d")
        raise ServerError() # 返回一个服务器错误，自定义

class Flask(_Flask):
    json_encoder = JSONEncode # 替换系统的jsonencode方法