import os

# 获取当前文件路径（相对路径）
f_path = __file__

# 获取当前文件路径（绝对路径）
f_path = os.path.abspath(__file__)

# 获取当前文件 所在目录(绝对路径)
dir_path = os.path.dirname(os.path.abspath(__file__))

# 路径字符串拼接 --注意这只是字符串，不代表路径真的存在。分隔符默认当前操作系统。
ROOT_PATH = os.path.join(dir_path, "..", "script")

# 添加 自定义模块（库）,就先添加路径到sys.path即可
sys.path.append(ROOT_PATH)

# 