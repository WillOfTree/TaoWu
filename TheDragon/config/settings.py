# -*- coding=utf-8 -*-
#-----------------------------------
# tornado.web.Application配置项:
# debug           ; debug模式，True/False
# static_path     ; 静态文件路径
# template_path   ; 模板路径
#
# cookie_secret   ; 安全字符串uuid
# xsrf_cookie     ; True
#
# secret_key      ; 安全字符串
# jwt_expire      ; 过期时间
#===================================
import os


settings = {
    "debug":True,
    # "secret_key": "1",
    # "jwt_expire": 6000,  # 这里必须是数字，不能是字符串
    # "MEDIA_ROOT": "./statics",  # 以server.py为基准
    # "static_path": os.path.join(os.path.dirname(__file__), "static"),
    # "template_path": os.path.join(os.path.dirname(__file__), "../templates"),
}

#-------------------------------
# redis配置项：
# host   ; IP地址
# port   ; 端口
#===============================
redis_config = dict(
    host='127.0.0.1',
    port=6379,
)

#-------------------------------
# mysql配置项：
# host      ; IP地址
# port      ; 端口
# user      ; 数据库登陆名
# password  ; 数据库登陆的秘密
# db        ; 数据库名称         
# charset   ; utf8 
#===============================
mysql_config = dict(
    database = "dragon",
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = ""
)


#---------------------
# 日志配置信息
#
#
#=====================



# 输出配置信息
try:
    if settings['debug'] and settings['template_path']:
        path = os.path.join(os.path.dirname(__file__), "../templates/")
        print("模板配置地址:{0}".format(path))
except KeyError:
    pass