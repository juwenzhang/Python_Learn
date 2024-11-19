# 设置一个 thread.local 的共享线程内的全局变量
# 然后设置两个线程，分别来实现设置这个 thread.local 的值，最后分别打印
# 确认每个线程的 thread.local() 的值是否相同
import time
from threading import local, Thread, currentThread

# 设置线程的全局数据
local_data = local()
local_data.name = "local_data"

class MyThread(Thread):
    def run(self) -> None:
        time.sleep(2)
        print("当前的子线程的名称赋值前为", currentThread(), local_data.__dict__)
        # 开始实现修改全局线程中的值
        local_data.name = self.getName()
        time.sleep(2)
        print("当前的子线程的名称赋值后为", currentThread(), local_data.__dict__)

if __name__ == "__main__":
    print("主线程的", local_data.__dict__)

    target01 = MyThread()
    target01.start()
    target01.join()


    target02 = MyThread()
    target02.start()
    target02.join()

    time.sleep(2)
    print("执行完后的值为", local_data.__dict__)