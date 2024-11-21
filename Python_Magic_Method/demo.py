class Person(object):
    # 开始给予一个标识来实现创建我们的单链模式
    __isinstance = False

    def __init__(self, name, age):
        """
        定义魔法方法一： 构造函数的书写
        初始化类的时候，该方法自动调度
        该方法调用的时机是在我们的对象已经被创建后，才实现的一个初始化对象属性的操作而已
        """
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        """
        开始实现定制化我们的类的介绍信息，这个方法来自于我们的 object 类
        我们如果需要返回一些自定义的信息的话，这个时候，我们就需要进行重写了
        打印实例对象的时候，该方法自动调度
        :return:
        """
        return f"Person_attr_list'[name={self.name}, age={self.age}]'"  # 描述的方式为: 类名[attr1=value, attr2=value]

    def __del__(self):
        """
        开始实现书写我们的析构函数,
        实例对象被销毁的时候，该方法自动调度
        :return:
        """
        print("对象被销毁了...")
        return "析构函数完成"

    def __new__(cls, *args, **kwargs):
        """
        用于实现的是我们的创建实例对象
        :param args:
        :param kwargs:
        """
        # 这一步就是说明的我们还没有实例化对象出来
        if not cls.__isinstance:
            cls.__isinstance = object.__new__(cls)  # 没有被创建过的话，那就直接实现我们的保存实例即可
        return cls.__isinstance  # 如果有实例，就实现直接返回实例即可，这样就可以保证我们的实例永远是同一个实例对象

    def __dir__(self):
        """
        该方法用来实现的是我们的查看对象的属性或者方法
        实现返回的是一个列表
        :return:
        """
        # 自定义需要返回给开发者人员观看的属性以及方法的
        return [self.age, self.name, self.__new__, self.__del__]

    def __getattr__(self, item):
        print(f"你进行访问的属性是:{item}")
        return "default"

    def __setattr__(self, key, value):
        if key == "age":
            if value < 18:
                raise Exception("age 设置的值必须大于 18")
            else:
                print(f"成功修改属性值，该属性为: {key}")
                self.__dict__[key] = value  # 就是实现的是当我们的属性的值正确的时候，直接实现赋值的操作即可
        else:
            print(f"成功修改属性值，该属性为: {key}")
            self.__dict__[key] = value  # 其他的属性直接赋值操作即可

    def __delattr__(self, item):
        print(f"销毁的属性为 {item}")
        return "default"

    def method_01(self):
        print("这个是第一个实例方法 method_01")

    def method_02(self):
        print("这个是第一个实例方法 method_02")




if __name__ == "__main__":
    # 开始实现实例化一个对象
    per = Person("76433", 18)
    print(per)
    print(per.__dir__())
    print(Person.__dict__)
    per.__dict__["name"] = "已经被修改了..."
    print(per.name)
    per.__dict__["id"] = "001"
    print(per.id)  # 001
    per.age = 111
    per.name = "水逆信封"


    str_test = "method_02"
    if hasattr(per, str_test):
        getattr(per, str_test)()


    if hasattr(per, "height"):
        setattr(per, "height", "1.88")
    print(getattr(per, "height"))

    if hasattr(per, "height"):
        delattr(per, "height")


    # 注意，这个里面必须是一段进行运算了的字符串
    print(eval("10 + 10"))