#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
iframe切换/窗口切换

frame元素或iframe元素的内部 会包含一个被嵌入的另一份html文档
缺省：是当前html
切换操作范围：切到嵌入的html

"""

from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建wddriver实例对象
wd = webdriver.Edge()


wd.implicitly_wait(10)

# 打开指定网址
wd.get("https://cdn2.byhy.net/files/selenium/sample2.html")
# 保存窗口句柄，方便切换
mainwndows = wd.current_window_handle
# 切换到内层html：wd.switch_to.frame(frame_reference)
# 这里填参数为：iframe的id，也可以填webelement对象
# wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR,"iframe[src='sample.html']"))
wd.switch_to.frame("frame1")

elements = wd.find_elements(By.CSS_SELECTOR, ".plant")
for element in elements:
    print(element.get_attribute("outerHTML"))


# 回到外层
wd.switch_to.default_content()
wd.find_element(By.ID, "outerbutton").click()


"""窗口切换
遇到连接跳转到新的窗口
wd.swithc_to.window()
wd.window_handles 所有窗口
"""
# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, "a")
link.click()

# 寻找窗口并切换到窗口
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if "Bing搜索" in wd.title:
        break

wd.find_element(By.ID, "sb from q").send_keys("白月黑羽")

# wd.title属性是当前窗口的标题栏，文本
print(wd.title)

# 切回窗口
wd.switch_to.window(mainwndows)


# 调试不让关闭页面
input()
