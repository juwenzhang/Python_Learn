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