import logging


def log(msg):
    # 创建logger日志器，如果参数为空则返回root logger
    logger = logging.getLogger("nick")
    logger.setLevel(logging.DEBUG)  #设置logger日志等级

    # 创建handler
    fh = logging.FileHandler("test.log", encoding="utf-8")
    ch = logging.StreamHandler()

    # 设置输出日志格式
    formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(filename)s %(message)s", datefmt="%Y/%m/%d %X")

    # 为handler指定输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 为logger添加的日志处理器
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 输出不同级别的log
    logger.info(msg)


log("泰拳警告")
log("提示")
log("错误")

# '''
# 分析：可以看到输出结果有重复打印
# 原因：第二次调用log的时候，根据getLogger(name)里的name获取同一个logger，而这个logger里已经有了第一次你添加的handler，第二次调用又添加了一个handler，所以，这个logger里有了两个同样的handler，以此类推，调用几次就会有几个handler。
# '''
