# ElementTree元素树
    import xml.etree.ElementTree as ElementET

## 读取"xml文件"
```python
# 1.读取"xml文件" 并获取"根元素"
tree = ET.parse(xml_path)
root = tree.getroot()
# 2.利用根元素找子元素 并修改文本
for v in root.iter("version"): # root.iter("tag名")为全局查找,且返回是一个迭代器需用for
    v.text = "23.0.2"
# 3.创建子元素
for copy in root.iter("copy"):
    copy[0].text = "123" # copy元素的第一个子元素，文本重新赋值
    copy[1].text = "456" # copy元素的第二个子元素，文本重新赋值
    source = ET.SubElement(copy,"source") # 给copy创建子元素source
    source.text = "/tmp/a.zip"
# 4.保存xml
tree.write(xml_path, "utf-8")
```
