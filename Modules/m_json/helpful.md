# json模块小技巧
一些关于json模块的小技巧统计在这里，方便在日后json解析过程中写出漂亮的代码

## 输出的json进行格式化（美化）
```python
    json.dumps(dic, sort_keys=True, indent=4, separators=(",", ":"))
    """
    1. dic: 就是要转化为json的对象,这里一般为字典
    2. sort_keys=True: 按字典(a-z)排序输出
    3. indent=4: 缩进4空格显示;读起来清晰
    4. separators=(",",":"): 指定分隔符;把字典里面的: 和,后面的空格都除去
    """
```