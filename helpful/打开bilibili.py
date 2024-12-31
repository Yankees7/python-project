#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
一键打开bilibili找到k8s开始学习
"""
from selenium import webdriver  # 初始化浏览器驱动
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By  # 寻找元素使用
from selenium.webdriver.common.action_chains import ActionChains

# 浏览器选项
# 设置一个用户数据目录，保证了selenum打开的web会保留数据--可免密
edge_options = Options()
edge_options.add_argument(r"--user-data-dir=D:\EdgeUserData")
# 分离选项；执行完毕不关闭浏览器
edge_options.add_experimental_option("detach", True)
# 创建webdriver对象
wd = webdriver.Edge(
    r"D:\\tools\\edgedriver_win64\\msedgedriver.exe", options=edge_options
)
# 隐型等待时间5s
wd.implicitly_wait(5)
# 设置浏览器窗口最大化
wd.maximize_window()
# 打开网址
wd.get("https://www.bilibili.com/")
"""示例：
# 选择搜索框输入k8s
input_element = wd.find_element(By.CSS_SELECTOR, ".nav-search-content > input")
input_element.send_keys("k8s")
# 选择搜索按钮并点击
search_element = wd.find_element(By.CSS_SELECTOR, ".nav-search-btn")
search_element.click()
# 选择热门并点击
hot_element = wd.find_element(By.CSS_SELECTOR, ".icon-bg__popular")
hot_element.click()
"""
# 选择收藏并点击
# favor_element = wd.find_element(By.CSS_SELECTOR, ".header-favorite-container__up")
# favor_element.click()

# 鼠标移动
ac = ActionChains(wd)
ac.move_to_element(
    wd.find_element(By.CSS_SELECTOR, ".header-favorite-container__up")
).perform()

# 选择Kubernetes收藏夹
element = wd.find_element(By.CSS_SELECTOR, "[title='Kubernetes']")
element.click()

#
element = wd.find_element(
    By.CSS_SELECTOR, "[data-mod='top_right_bar_window_custom_collection']"
)
print(element.get_attribute("outerHTML"))
