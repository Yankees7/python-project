"""
关于函数传参的使用
"""


# 函数调用时，传递的参数，写为key=value形式，称为：关键字参数
# 函数调用时，传递的参数, 直接写arg，称为：位置参数
def func1(name, age):
    print(f"{name} is {age} years old!")


print(func1("tom", 20))  # 位置参数
print(func1(age=20, name="tom"))  # 关键字参数
# 语法错误，只能位置参数在前，关键字参数在后
# print(func1(age=20,"tom")) # 位置参数和关键字参数


# 定义参数时，如果将函数的参数前加*,表示使用元组接受参数。
# 定义参数时，如果将函数的参数前加**,表示使用字典接受参数。
def func2(*args):
    print(args)


print(func2("hello"))
print(func2("hao", "123"))
print(func2("hao", "123", "tom", "jerry"))


def func3(**kwargs):
    print(kwargs)


print(func3())
print(func3(name="tom", age=20))


# 元组和字典都使用
def func4(*args, **kwagrs):
    print(args)
    print(kwagrs)


print(func4("tom", "jerry", dep="ops", sex="male"))
