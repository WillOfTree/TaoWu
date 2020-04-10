""" 程序启动文件
Flask_app 程序
midder 中间件
router 路由
"""
from System.App import create_app

#from System import Midder

if __name__ == '__main__':
    app = create_app()
    app.run()