""" 程序配置文件信息

配置初始化目录，配置flask项目参数
不包含数据库，redis配置；数据库redis配置查看db.py
"""
import os
import sys

# 添加请求位置到系统
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # 系统路径
static_dir = os.path.join(BASE_DIR, 'Public/static') # 静态目录
templates_dir = os.path.join(BASE_DIR, 'Public/templates') # 模板目录
sys.path.append(os.path.join(BASE_DIR, "../http"))
# sys.path.append(os.path.join(BASE_DIR, "../libs"))


DEBUG = True

