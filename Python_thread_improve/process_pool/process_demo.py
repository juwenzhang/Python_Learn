import multiprocessing
import time

def get_html(n: int) -> int:
    time.sleep(n)
    print("子进程获取内容成功:", n)
    return n

if __name__ == "__main__":
    # 通过 cpu_count 获取当前主机的核心数
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3,))

    pool.close()
    pool.join()

    print(result.get())
    print("end")