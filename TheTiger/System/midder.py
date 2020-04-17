"""
    中间件方法，用于拦截    
"""
from system import create_app
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





if __name__ == "__main__":
    pass