"""
    创建APP的方法
"""
from flask import Flask

from System.Router import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object("System.Config.setting")
    
    # 注册路由
    register_blueprints(app) 
    
    # 注册DB
    # db.init_app(app)
    # db.create_all(app=app)
    return app


if __name__ == "__main__":
    pass



