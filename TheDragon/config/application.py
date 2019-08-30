# -*-coding:utf-8-*-
#
# application
# 
# 模块初始化配置
# ------------
#
# 在application初始化时配置一些参数
# 如果没有配置mysql，redis，请注释掉 mysql、redis初始化代码

import tornado.web
import redis
import peewee_async

# 没有配置mysql、redis，注释
from .settings import redis_config
from .model import database


class Application( tornado.web.Application ):
    

    def __init__(self, *args, **kargs):
        super(Application, self).__init__(*args, **kargs)
       
        # 配置mysql
        # 没有配置注释掉
        database.set_allow_sync(False) # 关掉同步
        self.db = peewee_async.Manager(database) # 异步orm
       
        # 配置redis
        # 没有配置注释掉
        self.redis = redis.StrictRedis(**redis_config) # redis



