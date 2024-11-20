import time
from typing import Generator

def func_a():
    while True:
        print("我是 func_a 函数...")
        yield
        time.sleep(0.5)


def func_b(obj: Generator):
    while True:
        print("我是func_b 函数")
        obj.__next__()

func_b(func_a())