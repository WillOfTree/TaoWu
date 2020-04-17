"""
    错误信息
"""
from Exception import Base

class ApiError(Base):
    """
        错误提示样例
    """
    code = 401
    msg = "The requested URL was not found on thse server"
    error_code = 500


class ApiFormError(Base):
    """
        表单错误
    """
    code = 500
    msg = "" # 父类有添加msg参数的方法，这里不用配置
    error_code = 500

class NotFound(Base):
    code = 404
    msg = ""
    error_code = ""

class AuthFailed(Base):
    code = 404
    msg = ""
    error_code = ""

class Forbidden(Base):
    code = 403