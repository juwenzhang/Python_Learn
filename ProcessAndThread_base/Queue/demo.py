from queue import Queue
import threading
import time


def product(q):
    kind = ("猪肉", "白菜", "豆沙")
    for i in range(3):
        print(threading.current_thread().name, "我是生产者")
        time.sleep(1)

        q.put(kind[i % 3])
        print(threading.current_thread().name, "做完了")


def consumer(q):
    while True:
        print(threading.current_thread().name, "消费者准备消费了")
        time.sleep(1)

        t = q.get()
        print(f"消费者消费了 {t}")

# 就是生产者生产一个，消费者就消费一个

if __name__ == "__main__":
    q = Queue(maxsize=1)

    threading.Thread(target=product, args=(q,)).start()
    threading.Thread(target=consumer, args=(q,)).start()