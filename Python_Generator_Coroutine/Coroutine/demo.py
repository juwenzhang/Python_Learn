from typing import Generator

# 模拟的是服务器
def consumer():
    r = ""
    while True:
        n = yield r
        if not n:
            return
        print("consumer {}".format(n))
        r = "200 ok"

# 模拟的是客户端
def producer(c: Generator):
    c.send(None)
    n = 0
    while n < 10:
        n += 1
        print(n)
        r = c.send(n)
        print(r)

c = consumer()
producer(c)

# 客户端一直向服务器发送请求，并且也一直返回数据给客户端