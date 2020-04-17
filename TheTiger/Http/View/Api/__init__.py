"""
    初始化红图构造
"""
from flask import Blueprint

from .view import api

def api_blueprint():
    # api_v1 = Blueprint("api_v1", __name__, static_dir="", )
    api_v1 = Blueprint("api_v1", __name__)

    # 向蓝图注册当前视图
    # api.register(api_v1, url_prefix=None)
    api.register(api_v1)
    
    return api_v1