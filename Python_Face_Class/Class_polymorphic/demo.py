class Animal(object):

    def say(self):
        print("动物在叫...")


class Dog(Animal):
    def say(self):
        print("狗在叫...")


class Cat(Animal):
    def say(self):
        print("猫在叫...")


class Sleep(Animal):
    def say(self):
        print("羊在叫...")

def animal_say(animal: Animal) -> None:
    animal.say()

if __name__ == "__main__":
    animal_say(Dog())
    animal_say(Cat())
    animal_say(Sleep())
    animal_say(Animal())

    # 实现的是进行判断一个实例对象是否是一个类的实例
    # Return whether an object is an instance of a class or of a subclass thereof.
    print(isinstance(Dog(), Animal))
    print(isinstance(Animal(), Dog))