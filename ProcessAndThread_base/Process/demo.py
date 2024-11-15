from multiprocessing import Process  # 引入多进程模块
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

    print(f"{target_name} 进程任务已经启动了")
    print(res.read().decode()[1: 10])


if __name__ == "__main__":
    process01 = Process(target=get_web, args=("https://www.baidu.com/", "process01"))
    process02 = Process(target=get_web, args=("https://www.jd.com/", "process02"))

    process01.start()
    process02.start()