import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建客户端套接字对象

client.connect(("127.0.0.1", 8888))  # 绑定连接端口

while True:
    content = input("请客户端输入需要输入的内容>>>")
    client.send(content.encode())  # 发送信息

    data = client.recv(1024)
    print(data.decode())