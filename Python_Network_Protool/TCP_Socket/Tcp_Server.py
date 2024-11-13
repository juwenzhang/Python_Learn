# 首先进行实现我们的服务端的开发
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实现创建基于 TCP|IPV4 的服务器连接对象

server.bind(("0.0.0.0", 8888))  # 绑定 IP 地址 + 端口号

server.listen()  # 进行对客户端进行监听

sock_server, addr = server.accept()  # 接收客户端的请求，并且返回客户端连接对象，以及连接客户端的地址信息（阻塞方法）

while True:
    data = sock_server.recv(1024)  # 接收客户端发送的数据的字节大小
    print(data.decode())  # 使用十进制解码获取客户端发送的信息

    content = input("请服务端用户输入你需要输入的内容>>>")
    sock_server.send(content.encode())  # 发送二进制的数据格式给客户端

    server.close()  # 关闭服务端