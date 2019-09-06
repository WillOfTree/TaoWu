"""路由配置文件

引入app/HTTP下的模块，
"""
from app.HTTP.Api.IndexHandler import IndexHandler

urlpattern = [
    (r"/api/login", IndexHandler),
    (r"/", IndexHandler)
]
