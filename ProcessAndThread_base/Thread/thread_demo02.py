from threading import Thread
import urllib.request

# 直接继承即可
class MyThread(Thread):
    def __init__(self, name, url, *args, **kwargs):
        """
        构造函数的书写
        :param name:
        :param url:
        :param args:
        :param kwargs:
        """
        super().__init__()
        self.name = name
        self.url = url

    def run(self, *args, **kwargs):
        """
        重写父类的 run 方法，该方法是创建对象的时候自动添加到线程中的任务
        :param args:
        :param kwargs:
        :return:
        """
        userAgent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

        headers = {
            "User-Agent": userAgent
        }

        req = urllib.request.Request(self.url, headers=headers)
        res = urllib.request.urlopen(req)

        print(f"{self.name} 线程任务已经启动了")
        print(res.read().decode()[1: 10])

if __name__ == "__main__":

    # 创建线程实例对象
    target01 = MyThread("target01", "https://www.baidu.com/")
    target02 = MyThread("target02", "https://www.jd.com/")

    # 启动线程
    target01.start()
    target02.start()

    # 阻塞线程
    target01.join()
    target02.join()

    print("运行结束")