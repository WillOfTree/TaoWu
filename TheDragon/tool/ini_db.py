# -*-coding:utf-8-*-
"""

  用于数据表生成

  为了防止模块无法引入需要先进行sys.path.append，把项目目录导入系统，
  导入项目目录为止（server.py同级目录即可）
  
    运行：
    python ini_db.py

  需要安装相关模块(peewee)

"""
import sys 
sys.path.append('E:\\weixin\\TheDragon')

from peewee import MySQLDatabase

#=========================
# 导入要生成数据表的model
#========================
from apps.models.user import UserModel


if __name__ == "__main__":
    
    # 连接数据
    data_base = MySQLDatabase(
        database = "dragon", host = "127.0.0.1", port = 3306, user = "root", password = ""
    )

    # 添加自己的数据表
    data_base.create_tables([UserModel])