# codeing:utf-8
'''
自定义logging模块相关的使用
'''

import logging
import time


class Customlog:
    '''
    '''

    def __init__(self, logger=None):
        '''
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        '''
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime()
