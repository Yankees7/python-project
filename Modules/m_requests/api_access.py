"""
编写py程序接入api(天气网站)
"""

import pprint
import requests
import json

URL = "http://jisutqybmf.market.alicloudapi.com/weather/query"  # 这就是api调用地址
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Authorization": "7eb4167a225b403fbd9686d83266d8a4",
}
params = {"citycode": "101010100"}
r = requests.get(URL, headers=headers, params=params)
if r.ok is True:
    if len(r.text) != 0:
        data = json.loads(r.content.decode())
    else:
        data = r.text

if "data" in locals():
    pprint(data)
