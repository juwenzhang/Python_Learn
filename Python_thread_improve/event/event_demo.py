# 性能测试 —— 集合点，在我们的多线程的环境下面，我们通过设置集合点，
# 让这些集合点处于一个等待的状态，然后后面直接同时执行，这个时候就可以实现高并发的特性了
# 这样就可以实现我们对一个服务器实现一个并发的压力实现
# 同时对一个服务器发送出请求，从而达到最后的并发压力
import time
from threading import Thread, Event

class MyThread(Thread):
    def __init__(self, event, event_name):
        super().__init__()
        self.__event = event
        self.event_name = event_name

    def run(self):
        print(f"线程 {self.__event}-{self.event_name} 已经初始化完毕，随时准备启动...")
        # 设置线程阻塞
        self.__event.wait()
        time.sleep(2)
        print(f"线程 {self.__event}-{self.event_name} 开始执行了...")

if __name__ == "__main__":
    event = Event()
    threads = []

    # 开始实现创建十个自定义的线程
    [threads.append(MyThread(event, i)) for i in range(1, 101)]

    # 先实现清空已经存在的线程对象
    event.clear()
    [t.start() for t in threads]

    # 开始实现让我们的所有线程执行
    event.set()
    [t.join() for t in threads]

    print("集合点测试完毕...")