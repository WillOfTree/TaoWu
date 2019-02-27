import Framework

# a = Server.Server()
# a.main()
''''
1、启动Framework框架
2、将框架Framework传递给server
3、server绑定IP、端口
4、server.start
'''


def main():
    # 配置自己的路由信息
    urls = {
        "/": "one"
    }
    a = Framework.FrameWork(urls)
    a.start("127.0.0.1", 8000)


if __name__ == "__main__":
    main()
