# 本文介绍如何打开一个文件

## 1.创建并打开一个新文件（如果文件存在则清空）仅可写入
```python
import os
import stat
OS_FLAG = os.O_WRONLY | os.O_CREAT # 创建并打开一个新文件（文件存在则清空）仅可写入
STAT_FLAG = stat.S_IWUSR | stat.S_IRUSR # 拥有者具有读(R)写(W)q权限
fie_descriptor = os.open(file_path, OS_FLAG, STAT_FLAG)
with os.fdopen(fie_descriptor, "w", encoding="utf-8") as fobj:
    fobj.write("buildVersion=23.0.0")
```

## 2.读写一个文件
```python
import os
STAT_FLAG = stat.S_IWUSR | stat.S_IRUSR
fie_descriptor = os.open(file_path, OS_RDWR, STAT_FLAG) # OS_RDWR:以可读写的方式打开文件
with os.fdopen(fie_descriptor, "r+", encoding="utf-8") as fobj:
    dic = json.loads(f.read())
    dic["commonTool"]["source"]= "master"
    f.seek(0) # 读取指针偏移量置0（移动到开头）
    f.truncate() # 从0开始清空所有内容
    packge_json = json.dumps(dic, sort_keys=True, indent=4, separator=(",", ":")) # 转成具有格式美化的json数据
    f.write(packge_json )    
```


