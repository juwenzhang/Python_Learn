class Person(object):

    def __init__(self, name, age, *args, **kwargs):
        """
        :param name:
        :param age:
        :param args:
        :param kwargs:
        """
        self.__name = name
        self.__age = age

    # 开始实现定义一个用来实现外部访问的方法，来获取类中的数据
    def get_value(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        print(f"{self.__name}, {self.__age}")


    def set_value(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        self.__name = "433"


if __name__ == "__main__":
    # print(dir(Person("76433", 18)))  # 实现的是获取我们的一个对象中的属性的方法 dir()

    # 开始实例化一个对象
    per = Person("76433", 18)
    per.get_value()
    per.set_value()
    per.get_value()