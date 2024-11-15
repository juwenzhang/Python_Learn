# 理解函数即变量
def foo():
    print("foo 函数")
    bar01()

bar = foo

def bar01():
    print("bar01 函数")

if __name__ == "__main__":
    bar()