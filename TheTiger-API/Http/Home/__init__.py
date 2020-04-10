"""
    初始化红图构造
"""
from flask import Blueprint

from Api.view import api


def home_blueprint():
    home_v1 = Blueprint("home_v1", __name__)
    # 向蓝图注册当前视图
    home_v1.register(home_v1, url_prefix="")


if __name__ == "__main__":
    pass