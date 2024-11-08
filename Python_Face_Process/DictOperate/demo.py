dict_demo = {"name": "76433", "age": 18}

print(dict_demo)

# 实现获取字典中的元素
print(dict_demo["name"])

# 修改字典的值
dict_demo["name"] = "水逆信封"
print(dict_demo["name"])

# 添加字典键
dict_demo["class"] = "dict_demo"
print(dict_demo)

# 删除键值对
del dict_demo["class"]
print(dict_demo)

# 获取字典的长度
print(len(dict_demo))

# 实现字典的清空
# print(dict_demo.clear())

dict_demo01 = dict_demo.copy()
print(f"{dict_demo} 的内存地址为 {id(dict_demo)}")
print(f"{dict_demo01} 的内存地址为 {id(dict_demo01)}")

arrList = ["name", "age", "address"]
dict_demo03 = dict.fromkeys(arrList)
print(dict_demo03)

print(dict_demo.get("address", "不存在这个键"))
print(dict_demo.get("name", "不存在这个键"))

print("name" in dict_demo)
for key in dict_demo:
    print(dict_demo[key])

print(dict_demo.items())
for items in dict_demo.items():
    print(items)
    for item in items:
        print(item)

for key in dict_demo.keys():
    print(key)

for value in dict_demo.values():
    print(value)