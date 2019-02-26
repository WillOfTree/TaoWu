# coding
from Server import Server


class FrameWork(object):
    '''框架'''

    URLS = None

    def __init__(self, urls):
        self.URLS = urls  # 配置路由信息

    # def __call__(self, env, start_response):
    def application(self, env, start_response):
        '''
        __call__允许类像函数一样被调用，也可以替换成准确的函数名称
        例如application
        '''
        path = env.get("PATH_INFO", "/")  # 如果是空，则默认为根目录

        # 处理静态文件
        # 我想根据文件类型来确定是否为静态文件
        if path.endwith(".html"):
            return self.read_file(evn, start_response)

        if path.endwith(".html"):
            # 转发路由
            for key, value in self.URLS:
                if path == key:
                    return value(evn, start_response)

        # 文件不存在
        status = "404 Not Found"
        headers = []
        start_response(status, headers)

        return "Not Found"

    def start(self, ip, port):
        '''自动启动服务器'''
        Server.Server(ip=ip, port=port, framework=self.application)

    def read_file(self, evn, start_response):
        """读取本地文件"""

        dir_path = "./html" + evn.PATH_INFO
        body = None
        try:
            f = open(dir_path, "rb")
        except IOError:
            # 错误
            statue = "HTTP1.1 404 Not Found\r\n"
            body = "<h1>404 NOT FOUND</h1>"
        else:
            # 没有异常
            c = f.read()
            f.close()
            statue = "HTTP/1.1 200 OK\r\n"
            body = c.decode("utf-8")

        header = [
            ('Content-Type', 'text/html'),
            ('Server', 'TreeComputer')
        ]
        # ....
        start_response(statue, header)

        return body

    # def application(self, evn, start_response):
    #     """
    #     WSGI协议规定
    #     application函数用于返回body体，
    #     start_response:用于返回状态码与head
    #     evn:用户请求数据,是一个字典
    #     """
    #     header = [
    #         ('Content-Type', 'text/html'),
    #         ('Server', 'TreeComputer')
    #     ]
    #     start_response(
    #         "200 OK", header)
    #     body = self.one()
    #     return body


def one(self):
    """
    WSGI协议规定
    application函数用于返回body体，
    start_response:用于返回状态码与head
    evn:用户请求数据,是一个字典
    """
    content = [
        ('Content-Type', 'text/html'),
        ('Server', 'TreeComputer')
    ]
    start_response(
        "200 OK", content)
    body = datetime.now()

    return body


if __name__ == "__main__":
    FrameWork().one()
