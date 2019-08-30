# -*- coding=utf-8 -*-
#
# model
#
# 异步模型
# -------
#
# peewee-async基础model
# 异步操作数据库的方法，BaseModel基础类，
# 统一连接一个数据库

import peewee_async
from peewee import Model
from .settings import mysql_config

# 连接数据库
database = peewee_async.MySQLDatabase(**mysql_config)

#====================
# 基础模型
#====================
class BaseModel (Model):
    pass
    class Meta:
        # --连接指定数据库--
        database = database