# 开始实现书写我们的类

"""
需要注意的是： 我们的类中的 __init__ 和 __del__ 实际上的话，就是我们的两个魔法方法
只要我们进行了初始化一个对象后
那么最后就有这两个函数直接被运行了
构造函数: 构造函数用来实现的是进行实现初始化参数列表的
析构函数： 也是实现的是自动化运行，实现的是在对象被定义完后，直接实现释放空间即可
"""

class Person(object):
    # 开始书写我们的构造方法
    def __init__(self, name, age, stu_num, *args, **kwargs):
        """
        构造方法的书写
        :param name: 用来实现传入的参数姓名
        :param age: 年龄
        :param stu_num: 学生编号
        :param args: 剩余参数
        :param kwargs: 剩余参数
        """
        self.name = name
        self.age = age
        self.stu_num = stu_num

    def __del__(self, *args, **kwargs):
        """
        析构函数
        :param args: 剩余参数
        :param kwargs: 剩余参数
        :return:
        """
        del self.name
        del self.age
        del self.stu_num
        print("析构完成")

    def running(self, *args, **kwargs):
        """
        定义一个人具有的跑步的行为
        :param args: 剩余参数
        :param kwargs: 剩余参数
        :return: None
        """
        print(f"{self.name}坚持跑步到了{self.age}")

    def study(self, *args, **kwargs):
        """
        定义的是一个人具有学习的行为
        :param args: 剩余参数
        :param kwargs: 剩余参数
        :return: None
        """
        print(f"{self.name}具有学习能力")

if __name__ == "__main__":
    # 实现的是创建一个实例对象
    stu = Person("76433", 18, 13002307)
    stu.running()
    stu.study()