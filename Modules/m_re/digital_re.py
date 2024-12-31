"""
本文主要介绍版本号(数字)范围的正则表达式书写
实现匹配：^~1.5.[3-999]
核心:[0-9]表示单个数字,即先匹配1个数字,再匹配两个数字,最后匹配三个数字
补充: [0-9] == \d 表示单个数字
"""
import re

# 举例字符串
mini_ver = "1.5.356"
prefix = r"1\.5\."


"""
错误示范
第三位置的小版本号刚好为3位数,而它的第一位,刚好符合一位数的匹配规则,就不是我们想要的匹配效果
"""
result_list = re.findall(f"{prefix}(?:[3-9]|[1-9][0-9]|[1-9][0-9][0-9])", mini_ver)
print(result_list)

"""
1.正确匹配顺序,应该是多位数先匹配，1位数最后匹配
2.第3位置的小版本号，用()组合起来为一个整体但默认为优先展示，所以再加上?:取消优先展示
"""
pattern = re.compile(f"{prefix}(?:[1-9][0-9][0-9]|[1-9][0-9]|[3-9])")
result_correct = re.findall(pattern, mini_ver)
print(result_correct)
print("补充: 3-999的正确匹配正则为,100-999,10-99,3-9: [1-9][0-9][0-9]|[1-9][0-9]|[3-9]")