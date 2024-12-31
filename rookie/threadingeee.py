'''
展示线程编程
'''


import threading


def hello():
    '''打印hello world'''
    print('hello world')


if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=hello)  # 生成线程
        t.start()   # 启动线程
