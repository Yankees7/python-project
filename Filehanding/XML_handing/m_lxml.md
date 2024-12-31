# lxml三方模块
还支持支持XPATH路径
    from lxml import etree

## 读取XML文档
```python
# 1.读取xml文档
et = etree.parse(xml_path)
# 2.xpath定位元素
# 找到存在"属性localpath=ui"的元素，并找该元素的"属性revision"的值，返回的是一个列表
et.xpath("//*[@localpath='ui']/@revision")[0]
```

## 创建XML文档
```python
# 1.创建根节点
root = etree.Element("project")
# 2.创建子节点
root1 = etree.SubElement(root, "artifact")
# 3.创建文本节点
root1.text = "component"
# 4.创建属性节点
root1.attrib["branch"] = "master" # 或 root1.set('id','test_Id')
# 4.根元素转为元素树
tree = etree.Element(root)
# 5.保存XML
tree.write(xml_path, pretty_print=True, xml_declaration=True, encoding="utf-8")
```