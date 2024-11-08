import random

print("随机数字为 {}".format(random.random()))
print("随机数字为 {:.2f}".format(random.random()))

print("在 {} 和 {} 之间的随机整数为 {}".format(2, 10, random.randint(2, 10)))
print(f"随机的浮点数为{random.uniform(2, 34)}")

print(random.choice(["剪刀", "石头", "布"]))

arr = ["剪刀", "石头", "布"]
random.shuffle(arr)
print(arr)

print(random.sample(arr, 2))