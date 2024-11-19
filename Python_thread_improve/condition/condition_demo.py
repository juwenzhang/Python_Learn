# 模拟对话机制
import time
from threading import Condition, Thread

class MyThreadUser1(Thread):
    def __init__(self, cond: Condition, name: str) -> None:
        super().__init__(name=name)
        self.__cond = cond

    def run(self) -> None:
        # 实现获取锁
        self.__cond.acquire()

        print(self.getName() + ": 你好呀！！！...")  # 第一句话
        time.sleep(2)
        # 唤起其他处于 wait 状态的线程
        self.__cond.notify()
        # 实现的是让自己的处于阻塞状态，只有等待到了 notify 才可以继续执行
        self.__cond.wait()

        print(self.getName() + ": 今天你吃的啥！！！...")  # 第二句话
        time.sleep(2)
        self.__cond.notify()
        self.__cond.wait()

        print(self.getName() + ": 拜拜！！！...")  # 第二句话
        time.sleep(2)
        self.__cond.notify()

        # 释放锁
        self.__cond.release()



class MyThreadUser2(Thread):
    def __init__(self, cond: Condition, name: str) -> None:
        super().__init__(name=name)
        self.__cond = cond

    def run(self) -> None:
        # 实现获取锁
        self.__cond.acquire()

        self.__cond.wait()  # 先处于等待状态

        print(self.getName() + ": 你也好呀！！！...")  # 第一句话
        time.sleep(2)
        # 唤起其他处于 wait 状态的线程
        self.__cond.notify()
        # 实现的是让自己的处于阻塞状态，只有等待到了 notify 才可以继续执行
        self.__cond.wait()

        print(self.getName() + ": 吃的红烧肉！！！...")  # 第二句话
        time.sleep(2)
        self.__cond.notify()
        self.__cond.wait()

        print(self.getName() + ": 拜！！！...")  # 第二句话

        # 释放锁
        self.__cond.release()



if __name__ == "__main__":
    cond = Condition()

    user01 = MyThreadUser1(cond, "user01")
    user02 = MyThreadUser2(cond, "user02")

    # 注意，这里的话，只有对方在线你才可以发送消息，不在线发个锤子消息
    user02.start()
    user01.start()

    user01.join()
    user02.join()

    time.sleep(2)
    print("两人对话结束，拜！！！")