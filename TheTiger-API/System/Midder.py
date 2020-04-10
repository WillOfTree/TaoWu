"""
    中间件方法，用于拦截    
"""
from System.app import create_app
from Libs.Exception.ApiException import ApiError


app = create_app()

@app.before_request
def request_start():
    """
        全局拦截-请求开始的时候
    """
    print("befor_request")


@app.before_request
def request_end():
    """
        全局拦截-请求结束的时候
    """
    print("api_request")


@app.errorhandler(Exception)
def request_error(e):
    """
        全局拦截-请求错误的时候
        只有1.0才能捕捉所有异常
    """
    if isinstance(e, ApiError):
        return e
    else:
        # 位置错误-记录错误
        return e


if __name__ == "__main__":
    pass