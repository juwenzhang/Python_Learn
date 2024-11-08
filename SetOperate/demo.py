set_demo = {1, 2, 3, "string"}
print(set_demo)
# print(type(set_demo))  # TypeError: unhashable type: 'list'
print(f"集合的内存地址为: {id(set_demo)}")

set_demo.add("水逆信封")
print(set_demo)
print(f"集合的内存地址为: {id(set_demo)}")

set_demo.remove("string")
print(set_demo)
print(f"集合的内存地址为: {id(set_demo)}")

# set_demo.clear()
print(set_demo)
print(f"集合的内存地址为: {id(set_demo)}")


set_test_01 = {1, 2, 3, 6, 33}
print(f"{set_demo} 和 {set_test_01}集合的并集为 {set_demo | set_test_01}")
print(f"{set_demo} 和 {set_test_01}集合的交集为 {set_demo & set_test_01}")