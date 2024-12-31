"""
python类 魔术方法介绍
应该记住的有三个magic
"""

from collections.abc import Iterable
from typing import Any


class Book:
    def __init__(self, title, author) -> None:
        "构造器方法，实例化时自动调用"
        self.title = title
        self.author = author

    def __str__(self) -> str:
        "打印、显示实例时，将展示这个方法返回的字符串"
        return f"《{self.title}》"

    def __call__(self) -> Any:
        "实例像函数一样调用时，执行此方法中的代码"
        print(f"《{self.title}》是{self.author}编著的")


if __name__ == "__main__":
    linux = Book("Linux运维之道", "丁明一")
    print(linux)  # 调用__str__
    linux()  # 调用__call__
