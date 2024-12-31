'''
logging模块学习(内置)
基础常识：
1.日志是记录软件运行发生事件，很重要，关乎调试，故障分析定位等
2.日志等级: DEBUG,INFO,NOTICE,WARNING,ERROR,CRITICAL,ALERT,EMERGENCY
DEBUG: 详细信息很多
INFO: 关键事件
WARNING: 表名发生一些意外，未来可能会发生问题，软件还是正常运行
ERROR: 发生严重问题错误，软件不能执行一些工程
CRITICAL: 严重错误,表明软件不能运行了
'''
import logging

# 调用模块级别的函数，来创建对应级别的日志
# 默认日志级别为warnning级别及以上的才会被输出
# logging.debug("debug_msg")
# logging.info("info_msg")
# logging.warning("warning_msg")
# logging.error("error_msg")
# logging.critical("critical_msg")

# logging.basicConfig可调整日志级别、输出格式
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%Y-%m-%d  %H:%M:%S %a')
logging.info("info_msg")

# logging.basicConfig包含参数说明：
# filename 指定日志输出目标文件
# filemode 指定日志文件的打开模式，默认'a',只有filename有时生效
# format 指定日志输出格式字符串
# datefmt 指定日期/格式。
# level 指定日志器的日志级别

# format日志格式，自己百度
