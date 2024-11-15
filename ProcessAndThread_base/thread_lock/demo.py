from threading import Thread, Lock

# 先创建一个锁的对象
lock = Lock()

num = 10

# 开始实现演示我们的锁的概念了，先定义线程任务
def thread_test_get(target_name, *args, **kwargs):
    for i in range(10000000):
        # 添加锁
        # lock.acquire()

        with lock:
            global num
            num += 1
        # print(target_name, num)
        # 释放锁
        # lock.release()


def thread_test_post(target_name, *args, **kwargs):
    for i in range(10000000):
        # 添加锁
        # lock.acquire()

        with lock:
            global num
            num -= 1
        # print(target_name, num)

        # 释放锁
        # lock.release()


if __name__ == "__main__":

    target01 = Thread(target=thread_test_get, args=("存钱",))
    target02 = Thread(target=thread_test_post, args=("取钱",))

    target01.start()
    target02.start()

    target01.join()
    target02.join()

    print(num)
    print("任务结束")