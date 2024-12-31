"""打开斗鱼进入一起看"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def douyu_web():
    douyu_url = "https://www.douyu.com/"
    # 打开网址,并给网页加载时间
    wd.get(douyu_url)
    time.sleep(2)
    # 移动鼠标到 "分类" 元素
    element = wd.find_element(By.CSS_SELECTOR, ".public-DropMenu-link[href]")
    ac.move_to_element(element).perform()
    # 点击"全部分类"元素
    element = wd.find_element(By.CSS_SELECTOR, ".DropMenuList-linkAll")
    element.click()
    # 切换窗口"游戏直播_全部游戏直播_斗鱼直播"
    for handle in wd.window_handles:
        wd.switch_to.window(handle)
        if "游戏直播_全部游戏直播_斗鱼直播" in wd.title:
            break
    # 点击"一起看"
    time.sleep(2)
    element = wd.find_element(By.CSS_SELECTOR, '.Aside-menu-item[href="/g_yqk"]')
    element.click()


if __name__ == "__main__":
    # 1.对应浏览器指定分离选项,执行完不关闭网页
    # 添加用户数据目录,后续免密
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(r"user-data-dir=d:\\selenium\\chrome_user_data")
    # 2.浏览器驱动对象，隐形等待30s(find_element)
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(30)
    # 3.设置窗口最大化
    wd.maximize_window()
    # 动作
    ac = ActionChains(wd)
    # 网站测试
    douyu_web()
