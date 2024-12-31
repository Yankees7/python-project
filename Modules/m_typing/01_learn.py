#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright Huawei Technologies Co., Ltd. 2023-2050. All rights reserved.
"""
typing模块,添加类型注解,不会影响程序运行
定义型类型注解：
a: int=2,
b: list=["how","are","you"]


内置型类型注解：
def test(a: int): 形式参数注解
    pass


复合注解: []中括号里说明容器里面元素类型
from typing import Tuple,List,Dict,Set
names: list[str] = ["Germey","Guido"]
def vec2(x: T,y:T) -> Tuple[int,int,int]: 返回值注解（Tuple需要import引入）
    return x,y


typing常用类型
数字：int整型、float浮点型（long长整型）、bool布尔型、complex复数型
字符串：str字符串
列表：List
元组：Tuple
字典：Dict
集合：Set
另补充：
Iterable可迭代类型
Iterator迭代器类型
"""

from typing import List

names: list = ["yangjing", "alice"]


def greeting(names: list) -> List[str]:
    return names[0].split()


def test() -> None:
    a: int = 123
    print(a)


print(greeting(names))
print(test())
