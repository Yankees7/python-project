#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
CSS表达式：其他属性选择，和逻辑或
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


# 其他属性，用css表达式来选择
# [属性="值"]
# [属性]
# 组合限制：可以加上标签名限制：如：div[class="SKnet"] 选择所有标签名为div并且class属性值为SKnet的元素
# 加上class限制：.plant[name="SKnet"]
# span.copyright
elements = wd.find_elements(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
for i in elements:
    print(i.get_attribute("outerHTML"))

# 条件 或 用逗号表达,理解：,连接两个表达式
# .plant , .animal
# .plant , #bottom
# #t1 > span,#t1 > p :t1下面的所有span和p


# 条件 与 用


# 退出该网站
# wd.quit()

"""
在浏览器，验证css 表语法，验证号了在写代码
1.f12,ctrl+f
2.输入表达式
"""


# 调试不让关闭页面
input()
