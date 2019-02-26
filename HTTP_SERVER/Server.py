# coding:utf-8
import socket
import re

from multiprocessing import Process


class Server(object):
    """服务器"""

    RESPONSE = None
    SIP = None
    SPORT = None
    FRAMEWORK = None

    def __init__(self, ip='', port='', formework):
        self.SIP = ip
        self.SPORT = port
        self.FRAMEWORK = formwork
        print("Server运行一次")

    def run_pro(self, client):
        """处理客户端的请求函数"""

        # 读取文件head头
        # while True:
        #     res = client.recv(1024)
        #     if len(res) > 0:
        #         print(res)
        #     else:
        #         break

        res = client.recv(1024)
        env = self.analysisHerd(res)
        response = self.FRAMEWORK(env, self.start_response)

        # 拼接响应头
        # HTTP_BODY = self.RESPONSE
        # HTTP_START_LINE = file['mark']
        # HTTP_HEADERS = "Server:one\r\n\r\n"
        # response = HTTP_START_LINE + HTTP_HEADERS + HTTP_BODY

        # client.send(response.encode("utf-8")) #与下面一行代码等价
        client.send(bytes(response, "utf-8"))  # python3需要转换为字节传送

        client.close()

    def analysisHerd(self, st):
        """处理头文件"""

        # 这里要是直接使用str进行转换，得出来结果是\\r\\n
        str_frist_line = st.splitlines()  # 按行进行分割/r/n

        #b'GET /index.html HTTP/1.1'
        # 正则需要将Bytes类型转换为str类型
        path = re.match(
            r"\w+\s+(/[^\s]*)\s+", str_frist_line[0].decode("utf-8")
        ).group(1)

        # 确定框架需要使用的数据
        evn = {
            "PATH_INFO": path
        }

        return evn

    def run(self, SOCK):
        print("程序已开启。。。")

        while True:
            client_socket, client_ip = SOCK.accept()  # 获取客户端

            p = Process(target=self.run_pro, args=(client_socket,))
            p.start()
            # 因为子进程已经获取到了资源，所以主进程可以释放资源
            client_socket.close()

    # def main():
    def main(self):
        """
        1/为什么将此函数放到类中__init__会运行多次,造成只能使用一个套接字
        2/使用setsockopt设置复用套接字时，会出现出现程序无法进入子进程
        """
        # tcp协议
        SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许使用上一次的套接字
        # SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        SOCK.bind((self.SIP, self.SPORT))  # 绑定端口
        SOCK.listen()  # 监听

        self.run(SOCK)

    def start_response(self, status, header):
        '''
        WSGI协议规定的必要函数
        这个函数主要用于拼接状态码与请求头
        '''

        response = "HTTP/1.1 " + status + "\r\n"
        for h in header:
            #"%s: %s" %h这个语法很是骚气
            response += "%s: %s\r\n" % h

        self.RESPONSE = response


if __name__ == "__main__":
    s = Server()
    s.main()
