"""使用PIL中的ImageGrab模块简单,但是效率有点低
# PIL是Python Imaging Library,它为python解释器提供图像编辑函数能力。 ImageGrab模块可用于将屏幕或剪贴板的内容复制到PIL图像存储器中。
# PIL.ImageGrab.grab()方法拍摄屏幕快照。边框内的像素在Windows上以“RGB”图像的形式返回，在macOS上以“RGBA”的形式返回。
# 如果省略了边界框，则会复制整个屏幕
"""
from PIL import ImageGrab

# 截屏并保存
# bbox定义左上，右下像素的4元组 (left, upper, right, lower) = (left, upper, left+longth, upper+height)
img = ImageGrab.grab(bbox=(424, 229, 424 + 833, 229 + 180))
print(img.size[0], img.size[1])
img.save("screenshot1.jpg")
