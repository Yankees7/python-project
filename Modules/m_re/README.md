## re模块，内建模块，功能：通过正则表达式（regex），匹配处理字符串

正则表达式：regular expression

### compile函数，用于编译正则表达式，生成一个Pattern对象；
compile搭配匹配方法，相比一般直接使用匹配函数情况速度要快，但除非百万级的匹配，其实速度没啥影响

pattern = re.compile('正则表达式'，flags)
pattern.match(text)

### match函数


