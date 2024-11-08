str01 = "this is a string"
print(str01)
print(type(str01))

str02 = 'this is a string'
print(str02)
print(type(str02))

str03 = """
    this is a string 
    this is a string 
    this is a string
"""
print(str03)
print(type(str03))


# 切片操作
operator_str = "this is a our operators string"
print(operator_str[0: 13: 2])
# 就是实现的是截取所有
print(operator_str[: :])


# 求取字符串长度
print(len(operator_str))
# 获取指定字符串在原字符串中出现的次数
print(operator_str.count("i"))
print(operator_str.count(" "))

# 实现首字母大写
print(operator_str.capitalize())

# 查找指定字符下标
print(operator_str.find("is"))

# 替换原字符串内容为指定字符串，可以指定替换次数
print(operator_str.replace("is", "are"))

# 指定原字符串中的内容实现拆分
print(operator_str.split(" "))

print(operator_str.index(' '))

# 判断一个字符串是不是纯数字
print(operator_str.isdigit())

# 判断字符串是否含有一个大小写的字符,只要含有一个大写就是返回 false
print(operator_str.islower())
print(operator_str.capitalize().islower())

# 将原字符串全部变为小写
print(operator_str.lower())

# 将原字符串全部变为小写
print(operator_str.upper())

print(operator_str.startswith("t"))
print(operator_str.endswith("string"))

print(operator_str.strip(" "))
print(operator_str.rstrip("string"))
print(operator_str.lstrip("this"))