# -*- coding=utf-8 -*-
#---------------------
# 项目启动文件
#=====================
import tornado.ioloop
import tornado.httpserver
# import wtforms_json #wtfom配置

from system.application import Application
from config.urls import urlpattern
from config.settings import settings
from tornado.options import define, options

define("port", type=int, default=8000, help="端口")


if __name__ == "__main__":
    # options.logging = configs.log_level
    # options.log_file_prefix = configs.log_file
    # wtform_json.init() # 开启wtform
    options.parse_command_line()

    app = Application(urlpattern, **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    # windows不能为0
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()