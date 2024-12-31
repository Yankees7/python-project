"""
# PyQt比调用windows API简单很多，而且有windows API的很多优势，比如速度快，可以指定获取的窗口，即使窗口被遮挡。
# 需注意的是，窗口最小化时无法获取截图。
# 首先需要获取窗口的句柄。窗口句柄hwnd
pip install PyQt5
pip install pypiwin32
"""
from PyQt5.QtWidgets import QApplication
import win32gui
import sys


# 程序会打印窗口的hwnd和title，有了title就可以进行截图了。
hwnd = win32gui.FindWindow(None, "C:\Windows\system32\cmd.exe")

app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot2.jpg")


"""补充获取所有窗口的标题"""
hwnd_title = dict()


# 回调函数
def get_all_hwnd(hwnd, mouse):
    if (
        win32gui.IsWindow(hwnd)
        and win32gui.IsWindowEnabled(hwnd)
        and win32gui.IsWindowVisible(hwnd)
    ):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


# EnumWindows枚举窗体
win32gui.EnumWindows(get_all_hwnd, 0)

# print(hwnd_title.items())
for h, t in hwnd_title.items():
    if t != "":
        print(h, t)  # # 句柄hwnd
