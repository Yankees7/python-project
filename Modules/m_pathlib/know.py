"""
pathlib模块
标准库，用于处理文件路径和文件系统操作
它提供了一种面向对象的路径操作方式，使得代码更加清晰易读，并且避免了在不同操作系统下的路径分隔符问题。
"""

from pathlib import Path

"""Path类
Path类是pathlib模块的核心，用于表示文件系统路径
"""


# 获取当前工作目录
current_dir = Path.cwd()
print(current_dir)
# 获取当前用户主目录
home_dir = Path.home()
print(home_dir)

"""pathlib常用属性"""
Path.parents  # 返回所有上级目录的列表
Path.parent # 返回上级目录
Path.parts  # 分割路径，类似os.path.split()，不过返回元组
Path.suffix  # 返回文件后缀
Path.name # 返回文件名
"""常用基本方法"""
Path.is_dir()  # 判断是否是目录
Path.is_file()  # 判断是否文件
Path.exists()  # 判断路径是否存在
Path.open()  # 打开文件（支持with）
Path.resolve()  # 返回绝对路径
Path.cwd()  # 返回当前路径
Path.iterdir()  # 遍历目录的子目录或者文件
Path.mkdir()  # 创建目录
"""创建多级目录
parents=True 创建中间级父目录
exists_ok=True 目标目录存在时不报错
"""
Path.mkdir(parents=True, exists_ok=True)

Path.rename()  # 重命名路径
Path.unlink()  # 删除文件
Path.rmdir()  # 删除空目录（目录非空触发异常）
Path.joinpath()  # 拼接路径
Path.glob()  # 使用通配符匹配文件或目录

