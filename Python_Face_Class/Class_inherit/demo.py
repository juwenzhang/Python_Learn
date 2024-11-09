class Person(object):
    num = 200

    def __init__(self, name, age, *args, **kwargs):
        """
        构造方法，定义实例化属性
        :param args:
        :param kwargs:
        """
        self.name = name
        self.age = age

    def __del__(self, *args, **kwargs):
        """
        析构函数
        :param args:
        :param kwargs:
        :return:
        """
        print("析构函数完成...")

    def running(self, *args, **kwargs):
        """
        定义一个实例方法
        :param args:
        :param kwargs:
        :return:
        """
        print(f"{self.name} 会跑步，今年{self.age}岁！！！")

    @classmethod
    def class_method(cls, *args, **kwargs):
        """
        定义一个类方法
        :param args:
        :param kwargs:
        :return:
        """
        print("我是一个类方法")

    @staticmethod
    def static_method(*args, **kwargs):
        """
        定义静态方法
        :param args:
        :param kwargs:
        :return:
        """
        print("我是一个静态方法")


# 开始定义一个类来继承我们的 Person 类
class Student(Person):

    def studing(self, *args, **kwargs):
        print("我正在学习")


if __name__ == "__main__":
    stu = Student("76433", 18)
    # 直接实现调用父类中的方法
    print(stu.name)
    print(stu.num)
    stu.running()
    stu.class_method()
    stu.static_method()

    # 调用子类中自己书写的方法
    stu.studing()