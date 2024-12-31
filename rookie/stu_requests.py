'''
这是学习requests模块的py程序实例
'''

import requests

# 1. 获取文本内容;
URL1 = 'https://www.cnblogs.com/Mayfly-nymph/p/10660500.html'
r = requests.get(URL1)
print(r.text)
