# -*- coding: utf-8 -*-
'''
这是学习subprocess的笔记
'''
import subprocess
import sys
import logging

# 获取系统（windows）默认编码
codec = sys.getdefaultencoding()
print(codec)

# command line
cmd = ["cmd", "/c", "mvn package"]
cmd2 = ["dir"]
# subprocess
result = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdoutdata, stderrdata = result.communicate()
# 返回subprocess的执行结果
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%Y-%m-%d  %H:%M:%S %a')
logging.info(result.returncode)

# 可以吧subprocess写入文件
# with open("logging.txt", 'w', encoding="utf-8") as f:
#     f.write(stdoutdata.decode(codec))

logging.info(stdoutdata.decode('gbk'))

# 补充：
# 1.Popen.communicate(input=None)
# 和子进程交互：发送数据到stdin，并从stdout和stderr读数据，直到收到EOF。等待子进程结束。可选的input如有有的话，要为字符串类型。
# 此函数返回一个元组： (stdoutdata , stderrdata ) 。
# 2.sys.getdefaultencoding() 获取系统默认编码方式
