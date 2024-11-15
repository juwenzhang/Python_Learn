from multiprocessing import Queue
import multiprocessing
import time


def product(q):
    kind = ("猪肉", "白菜", "豆沙")
    for i in range(3):
        print(multiprocessing.current_process().name, "我是生产者")
        time.sleep(1)

        q.put(kind[i % 3])
        print(multiprocessing.current_process().name, "做完了")


def consumer(q):
    while True:
        print(multiprocessing.current_process().name, "消费者准备消费了")
        time.sleep(1)

        t = q.get()
        print(f"消费者消费了 {t}")

# 就是生产者生产一个，消费者就消费一个

if __name__ == "__main__":
    q = Queue()

    multiprocessing.Process(target=product, args=(q,)).start()
    multiprocessing.Process(target=consumer, args=(q,)).start()