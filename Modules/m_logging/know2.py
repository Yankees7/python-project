"""
logging模块学习(内置)
日志流处理流程：
logging日志模块四大组件：
1.日志器 Logger 提供了应用程序可一直使用的接口
2.处理器 Handler 将logger创建的日志记录发生到合适的目的输出
3.过滤器 Filter 提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
4.格式器 Formartter 决定日志记录的最终输出格式

logging模块就是通过这些组件来完成日志处理的，上面所使用的logging模块级别的函数也是通过这些组件对应的类来实现的
"""
import logging

# 创建logger，如果参数为空则返回root logger
logger = logging.getLogger("nick")
logger.setLevel(logging.DEBUG)  # 设置logger日志等级

# 创建handler
fh = logging.FileHandler("test.log", encoding="utf-8")  # 输出文件看需要添加
ch = logging.StreamHandler()  # 输出

# 设置输出日志格式
formatter = logging.Formatter(
    fmt="%(asctime)s %(name)s %(filename)s %(message)s", datefmt="%Y/%m/%d %X"
)

# 注意 logging.Formatter的大小写

# 为handler指定输出格式，注意大小写
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 为logger添加的日志处理器
logger.addHandler(fh)
logger.addHandler(ch)

# 输出不同级别的log
logger.warning("泰拳警告")
logger.info("提示")
logger.error("错误")

info = """
path=/usr1/workspace/
branch=master
"""
