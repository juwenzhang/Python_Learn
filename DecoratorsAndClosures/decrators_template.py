# 被装饰函数带有参数或者不带有参数
def decorator01(func):
    def run(*args, **kwargs):
        # 给函数附加的功能
        func(*args, **kwargs)
    return func


# 装饰器本身具备参数的情况
def decorator02(param):
    def outer_run(func): # 被装饰的函数名作为参数
        def inner_run(*args, **kwargs): # 被装饰的函数所需参数
            # 给函数附加的功能代码
            func(*args, **kwargs)
        return inner_run
    return outer_run


# 被装饰函数具备返回值
def decorator03(param):  # 装饰器本身所需参数
    def outer(func):
        def inner(*args, **kwargs):
            res = func()
            return res
        return inner
    return outer


# 我们的装饰器函数是可以在我们的完成一些功能的时候，直接抽象出一些工具函数来使用即可
# 这样就可以给自己的项目添加一些亮点了，这个就是抽离代码的好处