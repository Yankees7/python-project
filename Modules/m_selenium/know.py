"""
教程网址: www.byhy.net
selenium: 通过模拟人对网页操作，实现自动化的概念
关键是：打开网页之后的，寻找元素，也就是寻找操作的对象
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


"""示例一: 通过id寻找元素"""

"""创建webdriver实例对象
# 根据需要选择浏览器和对应驱动，已经加入环境变量path不需要指定驱动
web = webdirver.Chrome() # 创建chrome浏览器对象
web = webdirver.Chrome('D:\\tools\\edgedriver_win64\\msedgedriver.exe')
web = webdirver.Chrome(service=Service('D:\\tools\\edgedriver_win64\\msedgedriver.exe'))
"""
web = webdriver.Edge("D:\\tools\\edgedriver_win64\\msedgedriver.exe")  # 创建edge浏览器驱动对象

# web.get方法--打开指定网址
web.get("https://www.baidu.com")

# 根据id属性选择元素，返回的就是该元素对应的element对象
# kw 是百度搜索框的id
element = web.find_element(By.ID, "kw")
"""可以捕获元素不存在时情形
from selenium.common.exceptions import NoSuchElementException
try:
    element = web.find_element(By.ID, "kw3")
except NoSuchElementException:
    print('没有找到元素')
"""

# 通过element对象，就可以对页面元素进行操作了
# element.send_keys() 模拟输入
# element.clik()    模拟点击
element.clear()  # 清楚输入框已有字符
element.send_keys("python3\n")

# 退出该网站
# web.quit()

# 用格input()只是为了调试,因为即使不web.quit本程序执行完毕也会关闭网页。
input()
