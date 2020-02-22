""" 程序配置文件信息

配置初始化目录，配置flask项目参数
不包含数据库，redis配置；数据库redis配置查看db.py
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # 系统路径
static_dir = os.path.join(BASE_DIR, 'Public/static') # 静态目录
templates_dir = os.path.join(BASE_DIR, 'Public/templates') # 模板目录

# 将系统目录添加
sys.path.append(os.path.join(BASE_DIR, "Utils"))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)


class DevelopmentConfing(Config):
    DEBUG = True
    TESTING = True
