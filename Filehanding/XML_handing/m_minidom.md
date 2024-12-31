# minidom文档对象模型
    from xml.dom.minidom import parse,Document

## 读取"xml文档"
```python
# 1.读取"xml文档" 并获取"根节点"
doc = parse(xml_path)
root = doc.documentElement
# 2.根据tag名，查找节点
for i in root.getElementByTagName("alias"): # 全局查找alias节点，返回一个节点列表
    i.childNodes[0].data = "CMS" # i.childNodes 返回alias节点的所有子节点的集合，它的第一个子节点刚好为文本节点.data修改文本
```


## 创建"xml文档"