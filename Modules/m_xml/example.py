'''
从内存中创建xml文档
'''
import os
from xml.dom.minidom import Document

this_dir = os.path.dirname(os.path.abspath(__file__))

# 确定根节点,dependencies节点
base_doc = Document()
root = base_doc.createElement('project')
base_doc.appendChild(root)
node_dependencies = base_doc.createElement('dependencies')
root.appendChild(node_dependencies)

# 确定dependency节点
node_dependecy = base_doc.createElement('dependency')
node_dependencies.appendChild(node_dependecy)

# 创建文本节点（并给node_dependency加入文本节点）
node_dependecy.appendChild(base_doc.createTextNode('文本节点'))
# 给node_dependecy设置属性
node_dependecy.setAttribute('name', "str")

# xml写入文档
with open(f'{this_dir}{os.sep}dependency.xml', 'w', encoding='utf-8') as f:
    base_doc.writexml(f, addindent='\t', newl='\n', encoding='utf-8')
