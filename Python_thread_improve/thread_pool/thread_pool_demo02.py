import time
from concurrent.futures import ThreadPoolExecutor

# 实现创建我们的线程池对象，指定最大的线程池大小
executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=20)

def get_html(times) -> int:
    time.sleep(times)
    print("获取网页信息中...", times)
    return times

# 实现的是将我们的需要执行的线程投入线程池中进行使用,并不阻塞主线程，其是立即实现调用
task01 = executor.submit(get_html, 3)
task02 = executor.submit(get_html, 4)
task03 = executor.submit(get_html, 5)


time.sleep(3)
# 实现的是检查线程池中的任务是否完成，完成了就返回 True，否则就是返回 False
print(task01.done())

# 取消任务的执行，但是需要注意的一点是，该任务还没有被放入线程池中才能取消成功，返回 bool 值
print(task02.cancel())

# 实现的是获取任务的值，可以设置响应事件的设置，阻塞方法
print(task01.result(timeout=3))