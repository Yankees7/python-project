# 本文主要介绍一下文件的打开模式

## 一般的打开模式: r w a r+ w+ a+
以下函数的**模式**介绍<br>
- open("文件路径",模式, encoding="utf-8")
- os.fdopen("文件路径",模式, encoding="utf-8")

带有+号，可读可写，但另有区别<br>
带有b的，不需要考虑编码格式<br>

- r  以只读方式打开文件（默认的模式）
- rb 以二进制只读打开一个文件
- r+ 打开一个文件用于**读写**
- w  创建并打开一个文件（文件存在则内容清空）用于写入
- w+ 创建并打开一个文件（文件存在则内容清空）用于读写
- a  打开一个文件用于追加（如果文件不存在，创建新文件进行写入）。新的内容将会追加到已有内容之后(刚打开时的文件指针会直接放在文件的结尾)<br>
- a+ 打开一个文件用于追加（如果文件不存在，创建新文件进行读写）。新的内容将会追加到已有内容之后(刚打开时的文件指针会直接放在文件的结尾)<br>

## os.open()的flag（打开模式）
os.open(file, flags[, mode]) <br>
mode类似chmod,默认0777 --可以用stat.S_IREAD等替代 <br>
flags介绍：<br>
- os.O_RDONLY: 以只读方式打开
- os.O_WRONLY: 以只写方式打开
- os.O_RDWR: 以读写方式打开
- os.O_APPEND: 以追加的方式打开
- os.O_CREAT: 创建并打开一个新文件
- os.O_TRUNC: 打开一个文件并截断他的长度为零（必须有写权限）