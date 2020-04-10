"""
    错误信息
"""
from Libs.BaseException import BaseException

class ApiError(BaseException):
    """
        错误提示样例
    """
    code = 401
    msg = "The requested URL was not found on thse server"
    error_code = 500


class ApiFormError(BaseException):
    """
        表单错误
    """
    code = 500
    msg = "" # 父类有添加msg参数的方法，这里不用配置
    error_code = 500