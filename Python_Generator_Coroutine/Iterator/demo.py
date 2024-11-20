from itertools import count
import collections

counter = count(start=10)
print(type(dir(counter)[0]))

for i in range(101):
    print(counter.__next__())

# 实现判断一个对象是否是迭代器对象
print(isinstance(counter, collections.Iterator))  # True

arr = [1, 2, 3,4, 5]
# 实现将列表转化为可迭代对象
arr_iter = arr.__iter__()
print(arr_iter.__next__())  # 1
print(arr_iter.__next__())  # 2


# 在我们的迭代结束的时候，再进行迭代的话会出现一个小的问题就是： StopIteration 的报错的