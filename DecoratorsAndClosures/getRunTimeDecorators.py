import time

sum_num = 0

def get_runtime(fn):
    def run(name):
        start_time = time.time()
        fn(name)
        end_time = time.time()
        print(f"{fn} 函数的运行时间为: {end_time - start_time}")
    return run


# 装饰器的运行的实际原理是： get_runtime(func)(name)
@get_runtime
def func(name):
    global sum_num
    for i in range(1001):
        print(sum_num, i)
        sum_num += i
    print(f"求和为: {sum_num}", name)


if __name__ == "__main__":
    func("func")

