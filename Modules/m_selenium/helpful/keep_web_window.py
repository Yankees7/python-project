"""
Edge使用"分离"选项，实现浏览器完成任务后继续保持打开状态
chrome浏览器同理可行
"""

from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


# 对应浏览器指定选项(分离)
edge_options = Options()
edge_options.add_experimental_option("detach", True)
# 创建webdriver时，写入选项
wd = webdriver.Edge(
    r"D:\\tools\\edgedriver_win64\\msedgedriver.exe", options=edge_options
)
wd.implicitly_wait(10)  # find等待10

# 窗口最大化等后续任务完成后，不关闭浏览器窗口
wd.maximize_window()
wd.get("https://www.baidu.com")
element = wd.find_element(By.ID, "kw")
element.send_keys("python3\n")
