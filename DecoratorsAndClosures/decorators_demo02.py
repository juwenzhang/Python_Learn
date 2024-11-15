def foo(fn):
    def run():
        fn()
        print("哈哈哈")
    return run

@foo
def func():
    print("我是一个 func 函数")

if __name__ == "__main__":
    foo(func)()
    print("=======")
    func()