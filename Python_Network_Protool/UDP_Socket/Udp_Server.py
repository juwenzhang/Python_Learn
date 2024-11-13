import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建服务器对象

server.bind(("0.0.0.0", 8888))  # 绑定端口

while True:
    data, addr = server.recvfrom(1024)  # 接收数据以及客户端的地址信息
    print(data.decode())

    content = input("请服务端用户输入你需要输入的内容>>>")
    server.sendto(content.encode(), addr)  # 发送数据