import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建服务器对象

# client.connect(("127.0.0.1", 8888))
#
# client.send("hello server".encode())

while True:
    content = input("请客户端输入需要输入的内容>>>")
    client.sendto(content.encode(), ("127.0.0.1", 8888))

    data = client.recv(1024)
    print(data.decode())