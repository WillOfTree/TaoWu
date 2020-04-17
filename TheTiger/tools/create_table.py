# -*-coding:utf-8-*-
"""

  用于数据表生成

  为了防止模块无法引入需要先进行sys.path.append，把项目目录导入系统，
  导入项目目录为止（server.py同级目录即可）

    运行：
    python ini_db.py

  需要安装相关模块(sqlal)

"""
import sys

# 导入当前库目录
path = sys.argv[0] + "/../.."
print("path:{0}".format(path))
sys.path.append(path)
# =========================
# 导入要生成数据表的model
# ========================
from Http.Models import db
from System.App import create_app

# 必须引入表，不引入无法创建表
from Http.Models import User
from Http.Models import Goods
from Http.Models import Goods_image
from Http.Models import Category

if __name__ == "__main__":
    app = create_app()
    db.create_all(app=app)
