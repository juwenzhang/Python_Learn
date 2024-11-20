import time

def generators():
    print("hello")
    t = yield 5
    print("world")
    print(t)

generators().__next__()
generators().send(None)  # 传入 None 关键字实现激活生成器
generators().send(None)


demo = generators()
# 先实现激活
demo.send(None)
# 然后传递数据
time.sleep(3)
demo.send("demo")