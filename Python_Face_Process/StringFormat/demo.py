# 开始使用占位符实现格式话输出
print("大家好，我的岁数是: %d" % 15)
print("大家好，我的名字是: %s" % "76433")
str_name = "juwenzhang"
print("大家好，我的名字是: %s" % str_name)
print("大家好，我的名字是: %10s" % str_name)


# format 格式化输出
name = "水逆信封"
age = 18
print("大家好,我的名字是:{};  我的年龄是:{}".format(name, age))
print("大家好,我的名字是:{name};  我的年龄是:{age}".format(name="76433", age=18))
print("{:.2f}".format(3.2413343241))


# f-string 格式化输出格式
name01 = "juwenzhang"
age01 = 18
print(f"大家好，我的名字是{name01}, 我的年龄为{age01}")