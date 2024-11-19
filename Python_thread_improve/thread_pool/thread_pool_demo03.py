import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED

# 实现创建我们的线程池对象，指定最大的线程池大小
executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=20)

def get_html(times: int) -> int:
    time.sleep(times)
    print("获取网页信息中...", times)
    return times


# as_complete 可以实现的是一次性获取结果
urls = [3, 2, 3]
all_task = [executor.submit(get_html, url) for url in urls]

# 该方法实现的是首先返回的是先执行完的任务，然后是慢的任务
for item in as_completed(all_task):
    # 是一个阻塞的过程
    data = item.result()
    print("主线程中获取任务的返回值是:", data)


# map 方法实现的是作为映射，返回我们的结果,根据输入任务顺序来实现打印结果
for item in executor.map(get_html, urls):
    print(item)

# 让我们的主线程阻塞,等待其条件被满足后，主线程才开始执行
wait(all_task, return_when=ALL_COMPLETED)
print("本次任务完毕喔")