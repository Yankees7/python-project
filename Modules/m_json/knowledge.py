import json

"""
常见方法：
json.loads() --把其他类型对象（常用json等）转为python对象（例如：字典等），loads操作的是字符串
json.load    --把其他类型对象（常用json等）转为python对象（例如：字典等），load操作的文件流
json.dumps   --把python对象（例如字典）转为json
json.dump    --吧python对象（例如字典）转为json
"""

# json.loads把字符串转为字典
s = '{"name":"wade","age":54，"gender":"man"}'
print(json.loads(s)) # 打印：{"name":"wade","age":54，"gender":"man"}

# json.load读取文将文件将文件内容转为Python对象
with open('s.json','r') as f:
    s1 = json.load(f)
print(s1) # 打印：{"name":"wade","age":54，"gender":"man"}


