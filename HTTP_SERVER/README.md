# web协议说明
http运行在TCP/IP协议之上，程序与程序之间使用socket进行通信，一个tcp socket由一个IP地址和端口组成。

IP：IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”；127.0.0.1（10进制的写法）
端口：0-65535，其中端口0-1023是系统使用；


# HTTP请求头（文本）
HTTP method| sp |URL| sp |HTTP version|\r\n
header field name| : | field value\r\n
header field name| : | field value\r\n
header field name| : | field value\r\n
\r\n
body

# HTTP响应（文本）
status phrase：对状态码的描述。#
HTTP method| sp |status code| sp |status phrase|\r\n
header field name| : | field value\r\n
header field name| : | field value\r\n
header field name| : | field value\r\n
\r\n
body

# 请求流程--通过socket处理请求
1、等待某个人连接我们的服务器并向我们发送一个HTTP请求
2、解析该请求
3、了解该请求希望请求的内容
4、服务器根据请求抓取需要的数据（从服务器本地文件中读或者程序动态生成）
5、将数据格式化为请求需要的格式
6、送回HTTP响应