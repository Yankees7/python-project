#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
CSS Selector 语法选择元素,根据显示风格效果来选择元素
简言之: css表达式,"css selector", 语法表示: 选择哪些元素,显示什么样效果
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
wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")


# 通过ccs表达式 选择元素
# wd.find_element(By.CSS_SELECTOR, selector表达式)
elements = wd.find_elements(By.CSS_SELECTOR, ".plant")  # .class名
elements = wd.find_elements(By.CSS_SELECTOR, "span")  # tag标签
elements = wd.find_elements(By.CSS_SELECTOR, "#searchtext")  # #id值
for element in elements:
    print(element.get_attribute("outerHTML"))


"""选择子元素和后代元素
1.元素2 是 元素1 的直接子元素,找元素2,表达式: 元素1 > 元素2, 例如： #ok > .plant
多层级: 元素4,表达式: 元素1 > 元素2 > 元素3 > 元素4

2.元素2 是 元素1 的后代元素，表达式：元素1 元素2
多层级：元素4，表达式：元素1 元素2 元素3 元素4

3.混用
"""
elements = wd.find_elements(By.CSS_SELECTOR, "#container > div")
for el in elements:
    print(el.get_attribute("outerHTML"))

# elements = wd.find_elements(By.CSS_SELECTOR, "#layer span")
# for el in elements:
#     print(el.get_attribute("outerHTML"))

# elements = wd.find_elements(By.CSS_SELECTOR, ".plant span")
# elements = wd.find_elements(By.CSS_SELECTOR, "#container #inner11 > span")

# 退出该网站
# wd.quit()

# 调试不让关闭页面
input()
