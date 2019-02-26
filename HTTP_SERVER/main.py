import Framework

# a = Server.Server()
# a.main()
''''
通过Framework调用server
'''


def main():
    # 配置自己的路由信息
    urls = {
        "/": "one"
    }
    a = Framework.FrameWork(urls)
    a.start("", 8000)


if __name__ == "__main__":
    main()
