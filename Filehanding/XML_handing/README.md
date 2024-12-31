# Python解析xml

python有三种xml解析方式：SAX(simple API for XML)、DOM(Document Oject Model)、ElementTree

- DOM方式：中文译为文档对象模型，它将XML数据在内存中解析成一个树，通过对树的操作来操作XML
- SAX方式：SAX是一个用于处理XML事件驱动的模型，它逐行扫描文档，一边扫一边解析，对大型文档的解析拥有巨大优势。
- ElementTree方式：相较于DOM来说拥有更好的性能，与SAX性能差不多，API使用也很方便



