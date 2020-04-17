"""
    开发配置
"""
SQLALCHEMY_DATABASE_URL = "mysql+cymysql://root:@localhost/shoplow"
SECRET_KEY = ""

# 动态追踪修改设置，如未设置只会提示警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
#查询时会显示原始SQL语句
SQLALCHEMY_ECHO = False

SQLALCHEMY_COMMIT_TEARDOWN = True