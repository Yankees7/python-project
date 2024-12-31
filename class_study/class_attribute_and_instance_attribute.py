"""
类属性和实例属性
"""


# 类属性如果被重新赋值，是否会影响到类属性的引用？
class TestA:
    attr = 1


obj_a = TestA()

TestA.attr = 42
print(obj_a.attr)


# 实例属性如果被重新赋值，是否会影响到类属性的引用？
class TestB:
    attr = 1


obj_a = TestB()
obj_b = TestB()

obj_a.attr = 42
print(obj_b.attr)


# 类属性实例属性具有相同的名称，那么.后面引用将会是什么？
class TestC:
    attr = 1

    def __init__(self):
        self.attr = 42


obj_c = TestC()

# __dict__ 是一个类的特殊属性（隐藏属性），它是一个字典，用于存储类和实例的属性；
print(obj_c.__dict__)
print(obj_c.attr)


"""得出python属性的引用机制
python中属性的引用机制是由外而内的，当你创建了一个实例之后，准备开始引用属：
这时候编译器会先搜索该实例是否拥有该属性
如果有，则引用。
如果没有，将搜索这个实例所属的类是否有这个属性。如果有则引用，没有那就只能报错了
"""
