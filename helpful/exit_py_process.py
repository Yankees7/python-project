#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author ayentrance@gamail.com

"""介绍几种常见的退出py程序
1.sys.exit()
2.os._exit()
3.exit()/quit()
3.raise excpetionname(reason)
"""

# 1.sys.exit(arg)
# sys.exit() 会引发SystemExit异常来退出，但SystemExit不被认为是错误的异常
# arg参数可选，默认为0；0 被视为"正常退出"，非0视为"非正常退出"
# 还可以sys.exit("sorry googbye")

# 2.os._exit(n) 直接退出不抛异常，不执行相关清理工作，常用在子进程的退出

# 3.exit()/quit() 抛出SystemExit异常，一般在交互式shell中退出时使用

# 4. raise exceptionName(reason) ： raise抛出异常
# exceptionName: python异常错误类型名称
# reason：自定义
# 4.1 raise RuntimeWaring("y不能为零")
# 4.2 raise RuntimRuntimeWaring ： reason可以不填


"""补充：捕获所有异常
try:
    ...
except Exception as e:
    raise e
"""