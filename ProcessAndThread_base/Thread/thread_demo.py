import threading
import urllib.request

def get_web(url, target_name, *args, **kwargs):
    """
    定义的线程任务
    :param url:
    :param target_name:
    :param args:
    :param kwargs:
    :return:
    """
    userAgent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

    headers = {
        "User-Agent" : userAgent
    }

    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)

    print(f"{target_name} 线程任务已经启动了")
    print(res.read().decode()[1: 10])


if __name__ == "__main__":
    # 开始通过类构造器来实现创建线程
    target01 = threading.Thread(target=get_web, args=("https://www.baidu.com/", "target01"))  # 第一个线程
    target02 = threading.Thread(target=get_web, args=("https://www.jd.com/", "target02"))  # 第二个线程

    # 开始启动线程
    target01.start()
    target02.start()

    # 为了让我们的主线程等待子线程的运行完毕后在执行
    target01.join()
    target02.join()

    print("程序的运行结束")