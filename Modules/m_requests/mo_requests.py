'''
模块: requests
requests使用http方法: 1.get查看  2.post修改 ...
requests模块将每种http方法都封装成了一个函数,需要使用哪一种方法访问服务器,只要调用同名函数即可
'''

import json
import requests

# 1 获取文本内容;r.text
URL1 = "https://mirrors.huaweicloud.com/"
# r = requests.get(URL1)
# print(r.text)

# 2 获取非文本内容;r.content;例如：图片
URL2 = "http://pic1.win4000.com/wallpaper/a/584ba8f522661.jpg"
# r = requests.get(URL2)
# with open('D:\\tmp\\girl.jpg', 'wb') as fobj:
#     fobj.write(r.content)

# 3 获取json串（序列化数据）;r.json()
URL3 = "http://www.weather.com.cn/data/sk/101010100.html"
# r = requests.get(URL3)
# print(r.json())       # 查看json
# print(r.encoding)     # 查看当前编码
# r.encoding = 'utf8'   # 修改编码
# print(r.json())       # 查看json

# requests相关方法通过header传递请求头
URL4 = "http://www.jianshu.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20110101 Firefox/52.0"}
# r = requests.get(URL4, headers=headers)
# print(r.text)

# requests.get方法传参，使用params完成
URL5 = "https://www.sogou.com/web"
# params = {'query': 'linux'}
# r = requests.get(URL5, params=params)
# print(r.text)

# request.post发送数据时，使用data完成
URL6 = "https://weibo.com/"
data = {'query': 'linux'}
r = requests.post(URL6, data=json.dumps(data), timeout=1)
print(r.json())
