""" 程序启动文件
Flask_app 程序
midder 中间件
router 路由
"""
from System.App import create_app

#from System import Midder
app = create_app()

# @app.errorhandler(Exception)
# def request_error(e):
#     """
#         全局拦截-请求错误的时候
#         只有1.0才能捕捉所有异常
#     """
#     if isinstance(e, ApiError):
#         return e
#     if isinstance(e, HTTPException):
#         code = e.code
#         msg = emdescription
#         error_code = 1007
#
#         # 位置错误-记录错误
#         return ApiError(code, msg, error_code)
#     else:
#         return ApiError()

if __name__ == '__main__':
    app.run()