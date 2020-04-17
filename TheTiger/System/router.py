""" 配置项目路由信息（路由蓝图） 

1/重写redprint类,server/redprint.py
2/
"""

def register_blueprints(app):
    """
        路由注册方法，引入路由，注册
    """
    from Http import api_blueprint
    # 向蓝图注册红图
    app.register_blueprint(api_blueprint(), url_prefix="/api")
