#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
补充edge驱动下载地址: https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/?form=MA13LH#downloads
去Libing下载版本级统计表格: CleanCode→版本质量代码→质量分析→子系统/服务→旁边打勾全选→点击导出统计数据
"""

from selenium import webdriver  # 初始化浏览器驱动
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


def webdriver_init() -> object:
    """
    浏览器驱动初始化功能,返回wd对象\n
    驱动固定地址: D:\tools\WebDriver\msedgedriver.exe，如有浏览器更新请替换或直接取消改路径并设置环境变量path
    """
    # 浏览器选项
    # 设置一个用户数据目录，保证了selenum打开的web会保留数据--可免密
    edge_options = Options()
    edge_options.add_argument(r"--user-data-dir=D:\EdgeUserData")
    # 分离选项；执行完毕不关闭浏览器
    edge_options.add_experimental_option("detach", True)
    # 创建Service对象，指定msedgedirver路径
    service = Service(r"D:\tools\WebDriver\msedgedriver.exe")
    # 创建webdriver对象
    wd = webdriver.Edge(service=service, options=edge_options)
    # 隐型等待时间5s
    wd.implicitly_wait(5)
    # 设置浏览器窗口最大化
    wd.maximize_window()
    # 返回web驱动对象
    return wd


if __name__ == "__main__":
    # 创建webdriver
    wd = webdriver_init()
    # 打开网址
    wd.get("https://portal.tenxun.com/apps/29/bd5e95a5-7c91-47d5-99ab-379fdd802043")
    time.sleep(5)

    # 保存当前窗口句柄，方便切换
    mainwindows = wd.current_window_handle

    # 切换到内层html
    wd.switch_to.frame(
        wd.find_element(
            By.CSS_SELECTOR,
            "iframe[src='https://www.baidu.com/adfafas']",
        )
    )

    # 找 "质量分析" 元素
    wd.find_element(By.XPATH, '//*[@id="menu"]/li[2]').click()

    # 点击全选
    wd.find_element(
        By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div[4]/div[1]/table/thead/tr[1]/th[1]/div/label/span/span',
    ).click()

    # 点击导出规则详情
    wd.find_element(
        By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div[3]/div[1]/div/span[2]/span/button/span/span',
    ).click()
