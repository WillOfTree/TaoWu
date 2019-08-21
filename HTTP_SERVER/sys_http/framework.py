#
# 框架
# ----
# 
# 基于WSGI协议，实现了application函数
#
#   * def application(env, start_response):
#   *   start_response(200, [("content-type","text/html")])
#   *   return "<h1>ok</h1>"
# 
# 通过使用url中加载的view，调用view中的/application/pyindex.py中的文件


class FrameWork(object):

    static = None
    urls = None
    headers = [ # 设置响应头
        ("content-type", "text/html"),
        ("server", "python/server"),
        ("Access-Control-Allow-Origin", "*"),
        ("Accept-Language","zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2")
    ]

    def __init__(self, URL: dict, static:str="") -> None:
        self.urls = URL
        self.static = static

    def __call__(
        self, environ: object, start_response: any
    ) -> str:
        """一个符合WSGI协议的响应
        environ         server解析的所以http信息
        start_response  指定调用的方法
        """
        # 获取请求的信息
        path = environ.get("PATH_INFO")
        
        # 路由分发
        if path.startswith("/static"):
            # 静态文件
            file_name = path[7:]
    
            if not file_name.endswith(".html"):
                file_name += ".html"
            
            # 读取文件
            try:
                with open(self.static + file_name, "rb") as f:
                    info = f.read()
            except IOError:
                start_response("404", self.headers)
                return "静态文件未找到:{0}" . format(self.static + file_name)
            else:
                start_response("200", self.headers)
                return info.decode("utf-8")

        else:
            # 动态文件
            for url, hender in self.urls:
                if path == url[0]:
                    body = hender(environ)
                    start_response("200", self.headers) # 设置请求头

                    return body

        start_response("404", self.headers)
        return "404 Not Found"

        
