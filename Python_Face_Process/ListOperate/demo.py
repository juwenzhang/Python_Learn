# 开始实现定义我们的列表容器
list01 = [1, 2, "2", "4", {"name": "76433"}, [1, 34, "76433", 14234]]

print(list01)
print(type(list01))

# 开始实现通过下标来实现获取我们的元素
print(list01[len(list01) - 1][2])

# 实现对列表的遍历
for i in list01:
    print(type(i))

# 获取我们列表的长度
print(len(list01))

# 列表的乘法操作: 这个就是先了将列表批量的产生元素了（字符串也是有这个操作的）
list02 = [1, 3, 5, 7]
print(list02 * 10)

print(1 in list02)

print(max(list02))
print(min(list02))

# 向列表末尾添加内容
list02.append('水逆信封')
print(list02)

# 统计出现次数
print(list02.count(2))

# 向列表末尾添加另一个序列的多个值,一次性操作
list02.extend([1, 2, 4, 67])
print(list02)

# 寻找列表中的指定元素位置
print(list02.index("水逆信封"))

# 向列表的指定位置插入元素 insert
list02.insert(2, 3)
print(list02)

list02.pop()
print(list02)
list02.pop(2)
print(list02)

list02.remove("水逆信封")
print(list02)

list02.reverse()
print(list02)

list02.sort()
print(list02)
list02.sort(reverse=True)
print(list02)

# list02.clear()
print(list02)

list03 = list02.copy()
print(list03)

del list02
# print(list02)  // NameError: name 'list02' is not defined