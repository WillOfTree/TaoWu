"""
    创建APP的方法
"""
from flask import Flask

from System import register_blueprints
from Http.Models import db

def register_plugin(app):
    """注册插件"""
    from Http import db

    db.init_app(app) # 注册数据库


def create_app():
    app = Flask(__name__)
    app.config.from_object("Config.setting")
    app.config.from_object("Config.secure")
    
    # 注册路由
    register_blueprints(app) 
    register_plugin(app)

    return app


if __name__ == "__main__":
    pass



