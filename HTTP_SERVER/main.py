# -*- coding: utf-8 -*-  
#
# 启动程序
#
import os

from sys_http.framework import FrameWork
from sys_http.server import HTTPServer

# 导入路由
from application.pyindex import index

# 配置url
config_url = [
    (r"/", index)
]
# 静态文件目录
# 静态文件目录必须为 /static
static_path = os.getcwd() + "/static"

if __name__ == "__main__":

    app = FrameWork(config_url, static_path)
    http = HTTPServer(app)
    http.bind(8000)
    http.start()
