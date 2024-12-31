import logging


def log(msg):
    # 创建logger，如果参数为空则返回root logger
    logger = logging.getLogger("nick")
    logger.setLevel(logging.DEBUG)  #设置logger日志等级

    # 解决方案2：这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
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


def log1(msg):
    #创建logger，如果参数为空则返回root logger
    logger = logging.getLogger("nick")
    logger.setLevel(logging.DEBUG)  #设置logger日志等级

    #创建handler
    fh = logging.FileHandler("test.log", encoding="utf-8")
    ch = logging.StreamHandler()

    #设置输出日志格式
    formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(filename)s %(message)s", datefmt="%Y/%m/%d %X")

    #为handler指定输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    #为logger添加的日志处理器
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 输出不同级别的log
    logger.info(msg)

    #解决方案1，添加removeHandler语句，每次用完之后移除Handler
    logger.removeHandler(fh)
    logger.removeHandler(ch)


log("泰拳警告")
log("提示")
log("错误")
