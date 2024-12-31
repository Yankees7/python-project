"""
关于类的高级用法
"""


# 1.继承和多态
# 我们定义了一个Animal基类和两个派生类Cat和Dog,这两个派生类继承了speak方法，并对他们进行了重写。
# 当我们实例化一个Cat或Dog对像，并调用speak方法时，程序会根据对象类型调用相应的方法。这种现象称为多态。
class Animal:
    def speak(self):
        print("Animal is speaking...")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Dog(Animal):
    def speak(self):
        print("Woof!")


# 多态是 Python 中另一个非常重要的面向对象特性。它允许不同的对象对相同的消息做出响应，即使它们的类型不同
c = Cat()
c.speak()
d = Dog()
d.speak()


# 2.类装饰器：类装饰器是修饰 类的函数 或 类，可以用于修改类的行为或元数据。启动比较常见的装饰器是
# @classmethod 和 @staticmethod
# 虽然@classmethod和@staticmethod非常相似，但它们在用法上有轻微的区别：classmethod必须将一个类对象的引用作为第一个参数，而staticmethod可以不带任何参数。
class Myclass:
    count = 0

    def __init__(self) -> None:
        Myclass.count += 1

    @classmethod
    def get_count(cls):  # 第一个参数是类
        return cls.count  # @classmethod 调用属性，直接第一个参数.属性名

    @staticmethod
    def hello():  # 可以不需要任何参数，当普通函数使用
        print("Hello World!")
        print(Myclass.count)  # @staticmethod调用类属性，必须：类.属性名


m1 = Myclass()
m2 = Myclass()

print(Myclass.get_count())
Myclass.hello()


# 3.属性装饰器
# 属性装饰器是 修饰类属性（方法名==属性名）） 的函数，可以用于对属性的读写和写入进行控制，便于对属性操作的同时完成其他的动作，包括限制访问权限、动态计算属性值等
# 例如：在获取、设置和删除对象属性的时候，需要额外做一些工作。比如在游戏编程中，设置敌人死亡之后需要播放死亡动画。
"""
@property 语法糖提供了比 property() 函数更简洁直观的写法。

被 @property 装饰的方法是获取属性值的方法，被装饰方法的名字会被用做 属性名。
被 @属性名.setter 装饰的方法是设置属性值的方法。
被 @属性名.deleter 装饰的方法是删除属性值的方法。
"""


class Person:
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        print("获取属性时执行的代码")
        return self._name

    @name.setter  # 设置属性
    def name(self, value):
        print("设置属性时执行的代码")
        self._name = value

    @name.deleter
    def name(self):
        print("删除属性时执行的代码")
        del self._age


p = Person("Alice")  # 设置属性时；同时要执行类定义的属性装饰器修饰的方法
print(p.name)  # 获取属性时；同时要执行类定义的属性装饰器修饰的方法

p.name = "Bob"  # 设置属性时；同时要执行类定义的属性装饰器修饰的方法
print(p.name)

# 4.上下文管理器器
# 上下文管理器是支持with语句的对象，--这就是解释了with open() as f:的原理由来。可以用于控制代码块的上下文行为。
# 在python中，实现上下文管理器需要定义两个方法 __enter__ 和 __exit__


class OpenFile:
    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, tranceback):
        self.file.close()


with OpenFile("test.txt", "w") as f:
    f.write("Hello world!")

"""
在上述代码中，我们定义了一个 OpenFile 类，它接受两个参数 filename 和 mode，并在 __enter__ 方法中打开文件，并在 __exit__ 方法中关闭文件。
然后我们使用 with 语句创建一个上下文管理器，并在代码块中使用文件对象 f 写入一些数据。由于使用了上下文管理器，在代码块结束时，程序会自动关闭文件，而不需要手动调用 close 方法。
"""


# 5.元类
# 元类是创建类的类，可以用于控制类的创建过程，包括修改类的属性和方法、验证类的结构和行为等。
# 在python中，可以通过编写元类来实现自定义类的创建方式
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class...")
        if "x" not in attrs:
            attrs["x"] = 100
        return super().__new__(cls, name, bases, attrs)


class Myclass(metaclass=MyMeta):
    y = 200


print(Myclass.x)
"""在上述代码中，我们定义了一个元类 MyMeta，它重写了 __new__ 方法，并在其中添加了一些自定义逻辑。然后我们定义了一个类 MyClass，并将其元类指定为 MyMeta。当我们实例化 MyClass 对象并调用 x 属性时，程序会自动执行元类的 __new__ 方法，并输出一条信息，同时在类定义中添加了一个新的属性 x 并赋初始值 100。
"""
