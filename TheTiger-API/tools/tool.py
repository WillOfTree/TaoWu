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

# 导入当前库目录
path = sys.argv[0] + "/../.."
print("path:{0}".format(path))
sys.path.append(path)
# =========================
# 导入要生成数据表的model
# ========================
from peewee import MySQLDatabase

# from models.UserModel import User
# from models.ExchangeModel import Exchange
# from models.TicketModel import Ticket
# from models.UserModel import AdminUser
from models.GoodsModel import Goods
from models.GoodsCategoryModel import GoodsCategory
from models.OrderInfo import OrderInfo


if __name__ == "__main__":

    # 连接数据
    data_base = MySQLDatabase(
        database="dragon", 
        host="127.0.0.1", 
        port=3306, 
        user="root", 
        password="root"
    )

    # 添加自己的数据表
    data_base.create_tables([
      # Exchange, Ticket
      # AdminUser
      # Goods,
      # GoodsCategory
      # OrderInfo
    ])
