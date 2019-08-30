# -*-coding:utf-8-*-
#
# urls
# 
# 路由（总）集合
# ------------
# 
# 配置路由信息

from apps.api.index import IndexHandler

urlpattern = [
    (r"/api/login", IndexHandler),
    (r"/", IndexHandler)
]
