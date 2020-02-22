""" 数据库配置方法

数据库链接-- pip install Peewee
redis-- pip install redis
"""
#import redis
from peewee import MySQLDatabase, Model


###-----------------------------------------
""" MySQL 连接参数配置 """
Database_name = ""
Database_host = ""
Database_port = ""
Database_user = ""
Database_passwd = ""
###-----------------------------------------
""" redis 配置参数 """

###-----------------------------------------



###-----------------------------------------
# mysql连接方法
def db():
    return MySQLDatabase(
        database = Database_name,
        host = Database_host,
        port = Database_port,
        user = Database_user,
        passwd = Database_passwd
    )
###------------------------
        
###-------------------------
# peewee 基础类
class BaseDB(Model):
    class Meta:
        database = db()
###-------------------------