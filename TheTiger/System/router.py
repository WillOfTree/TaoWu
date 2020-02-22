""" 配置项目路由信息（路由蓝图） 

1\创建蓝图，Blueprint("api", __name__)
2\向app中注册蓝图， 
3\view视图中引入配置的蓝图，@api.route("/route")

蓝图不会默认注册静态目录的路由, 需要使用static_folder传参数
"""
from System import Flask_app

from App.view import api

# 注册蓝图
Flask_app.register_blueprint(api)