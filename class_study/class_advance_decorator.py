"""
类装饰器(decorator)
"""


class Date(object):
    logo = "name"

    def __init__(self, day=0, month=0, year=0) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split("-"))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split("-"))
        return day <= 31 and month <= 12 and year <= 3999

    @staticmethod
    def test1():
        print(Date.logo)

    @classmethod
    def test2(cls):  # cls指类本身
        print(cls.logo)  # 如果此方法用到了其他类的属性和方法，classmethod更适合，避免硬编码


date2 = Date.from_string("25-06-2024")  # @classmethod主要场景是完成：实例化时的预处理（对参数的预处理）
is_date = Date.is_date_valid("25-06-2024")

# 如果是类.方法，两者并无区别，反而classmethod更好，避免硬编码（如果才用@staticmethod，子类继承并且子类对属性或方法有重写，这时还是指向的父类）
# @staticmethod 和@classmethod 无论是类和实例都能直接调用
print(date2.test1())
print(date2.test2())
