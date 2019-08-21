#
# WSGI协议的服务器端
# ----------------
#
# 用于监听端口，获取端口的http请求，把请求调用Framework中的
#

import socket
import re

from multiprocessing import Process


class HTTPServer(object):
    
    application = None
    SOCK = None

    def __init__(self, app:object)->None:
        """初始化参数，端口
        启动时监听网路数据
        IP   监听的IP
        port 监听的端口
        """
        # socket.AF_INEF 
        # socket.SOCK_STREAM 
        try:
            self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except:
            print("启动失败")
            exit(0)

        # 加载框架
        self.application = app


    def start(self)->None:
        """主循环等待客户端连接"""
        self.SOCK.listen()
        while True:
            client_socket, client_ip = self.SOCK.accept() # 监听端口
            p = Process(target=self.run_pro, args=(client_socket,))
            p.start() # 启动子进程
            client_socket.close() # 释放进程
    

    def bind(
        self, PORT:any=8000, IP:str="127.0.0.1"
    )->None:
        """绑定端口，IP"""
        self.SOCK.bind((IP, PORT))
        
        print("程序已启动动成功!")
        print("IP:{0}---PORT:{1}".format(IP, PORT))


    def run_pro(self, client:object)->None:
        """子进程处理函数"""
        # client  socke接入的客户端
        
        res = client.recv(1024)    

        # 处理不同的文件头
        str_info = res.splitlines() # 根据\r\n切割字符串
        
        # b'GET /index.html HTTP/1.1'
        # 正则需要将Bytes类型转换为str类型
        path = re.match(
            r"\w+\s+(/[^\s]*)\s+", str_info[0].decode("utf-8")
        ).group(1)

        # 组成WSGI的环境信息
        env = {
            "PATH_INFO":path,
            "METOD": "GET"
        }
        # 打印请求信息
        print(str_info[0].decode("utf-8"))

        # 调用框架，传递信息
        body = self.application(env, self.__start_response)
        # 返回数据设置header
        response = self.response_headers + "\r\n<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />" + body
        
        client.send(bytes(response, "utf-8"))
        client.close()


    def __start_response(self, status:str, headers:any)->None:
        """回调函数，拼接响应头"""

        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header

        self.response_headers = response_headers


if __name__ == "__main__":
    HTTPServer("127.0.0.1", 8000, {"/":"index"})