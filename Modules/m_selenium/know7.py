#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
1.CSS表达式：按次序选择子节点（父亲的第几个儿子）
2.兄弟节点的选择
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


"""
等待元素出现
"""

# 创建wddriver实例对象
wd = webdriver.Edge()
wd.implicitly_wait(10)

# 打开指定网址
wd.get("https://cdn2.byhy.net/files/selenium/sample1b.html")


# 父元素的第n个子节点
# span:nth-child(2) span为它父元素的第二个节点
# :nth-child(2) 只要是它父元素的第二个都会被选中
# #t1 > span:nth-child(2)
elements = wd.find_elements(By.CSS_SELECTOR, "span:nth-child(2)")
for i in elements:
    print(i.get_attribute("outerHTML"))

# 父元素的倒数的几个子节点
# :nth-last-child(1) 倒数第一个子元素
# p:nth-last-child(1) p为倒数第一个子元素

# 父元素的某类型的第几个子节点
# span:nth-of-type(1) # 第一个span类型的子元素 == span:nth-child(2) 这里的例子相等而已
# span:nth-last-of-type(1) # 倒数第一个span类型子元素

"""奇数点和偶数点
奇数：:nth-child(odd)
偶数：:nth-child(even)
p类型的奇数和偶数
p:nth-of-type(odd)
"""


# 退出该网站
# wd.quit()

"""
在浏览器，验证css 表语法，验证号了在写代码
1.f12,ctrl+f
2.输入表达式
"""

"""兄弟节点的选择，紧跟的关系
h3 + span：选择h3紧跟的那一个span
h3 ~ span：选择h3后面的所有span
#t1 h3 ~ span
"""

# 调试不让关闭页面
input()
