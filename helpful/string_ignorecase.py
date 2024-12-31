"""
判断字符串忽略大小写
"""
import re
import logging as log

log.basicConfig(level=log.INFO)


# 1.使用正则表达式,使用IGNORECASE标志
UPBVERSION = "smartkit 23.0.0.B016"
if re.match("SmartKit", UPBVERSION, re.IGNORECASE):
    log.info("以smartkit开头的为B版本")


# 2.比较前把两个字符串，都转成同样大写或同样小写
s1 = "smartkit"
s2 = "SmartKit 23.0.0.B016"
if s1.lower() in s2.lower():
    log.info("包含smartkit是B版本")

if s1.upper() in s2.upper():
    log.info("包含smartkit是B版本")
