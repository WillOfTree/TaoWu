# -*- coding=utf-8 -*-
"""
  数据表生成
"""
from config.model import BaseModel
from peewee import *

class UserModel (BaseModel):
    mobile = CharField(max_length=11, verbose_name="手机号码", index=True)

    class Meta:
        # 数据库名
        # db_table = "user"
        table_name = "user"