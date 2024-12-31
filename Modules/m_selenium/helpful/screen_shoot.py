from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image

"""全局截图"""
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# # 打开网址
driver.get("https://www.baidu.com")
driver.maximize_window()
# # 截屏保存为图片文件
# driver.get_screenshot_as_file("screen_shoot_1.png")
# driver.save_screenshot()

"""局部截图"""
# t = time.time() 时间戳
t = time.strftime("%Y-%m-%d_%H:%M:%S")
picture_name = str(t) + ".png"

# 获取 整个网页截图
driver.save_screenshot("baidu.png")
# 定位 百度一下 按钮
imgcode = driver.find_element(By.CSS_SELECTOR, "#kw")
# location方法获取元素坐标值x,y且以字典的方式返回
left = imgcode.location["x"]
top = imgcode.location["y"]
# size方法获取元素的高度和宽度，以字典方式返回
right = left + imgcode.size["width"]
bottom = top + imgcode.size["height"]
# 打开整个网页截图
im = Image.open("baidu.png")
# 获取登录按钮截图
mg = im.crop((left, top, right, bottom))
# 保存截图,命名为ann
mg.save("ann.png")
