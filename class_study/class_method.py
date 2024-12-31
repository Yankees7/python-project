"""
类的方法学习
"""


class CocaCola:
    formula = ["caffeine", "sugar", "water", "soda"]

    # 方法就是函数，但我们把这个函数称之为方法；方法是给实例使用的，还可以称之为实例方法；
    # self这个参数就是被创建的实例本身;被实例化的对象，被编译器默默的传入后面方法的括号中，作为第一个参数；self可以随意更改名称，这里只是习惯用self
    def drink(self) -> None:
        print("Energy!")

    def drink_howmuch(self, how_much) -> None:  # 更多参数
        if how_much == "a sip":
            print("cool!")
        if how_much == "whole bottle":
            print("Headache!")

    """存在一些方法被称为“魔术方法”；例如：__init__() 初始化，它在创建实例后时候自动执行，因为能自动处理很多事情，常用于新增实例属性
    """

    def __init__(self) -> None:
        pass

    # def __init__(self, logo_name) -> None:  # __init__()方法自己的参数
    #     self.logo_name = logo_name


coke = CocaCola()
coke.drink()  # coke.drink() == CocaCola.drink(coke)

ice_coke = CocaCola()
ice_coke.drink_howmuch("a sip")
