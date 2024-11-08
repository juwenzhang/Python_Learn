def func(*args, **kwargs) -> None:
    """
    函数的一个简单的书写
    :param args: 可选参数
    :param kwargs: 可选参数
    :return: None
    """
    print(type(args), type(kwargs))
    print("我是函数")

# 实现获取我们的函数的注释内容
print(func.__doc__)
# 开始函数的调用
func()

def func01(age: int, name="76433", *args, **kwargs) -> None:
    """
    函数定义
    :param age:
    :param name:
    :return:
    """
    print(f"我的年龄为{age},我的名字是{name}")
    print(args, kwargs)

func01(18)
func01(18, "水逆信封", 12, 23, 43, value="水逆信封", token="我是访问令牌")

def func03(num):
    """

    :param num:
    :return:
    """
    num = 10
    print(num)

num = 20
func03(num)
print(num)


def func04(dict_demo):
    dict_demo["class"] = "hahaha"
    print(dict_demo)

dict_demo = {"name": "juwenzhang"}
func04(dict_demo)
print(dict_demo)


sum_demo = 0
def func04(a, b):
    global sum_demo
    sum_demo = a + b
    print(sum_demo)
    return sum_demo
func04(10, 20)
print(sum_demo)

# func 就是我们的匿名函数的指针
func05 = lambda x, y: x + y
print(func05(10, 30))

func06 = lambda : print("hello world")
func06()


mylist = [{"name": 23}, {"name": 12}, {"name": 53}]
print(list(mylist[0].values())[0])
mylist.sort(key=lambda item: list(item.values())[0])
print(mylist)