'''
多线程threading
捕获子线程异常，退出
'''
from time import ctime
import threading
import time
import queue
import sys


def a():
    ''''''
    try:
        # for i in range(5):
        print('Program a is running... at ', ctime(), u'.线程名为：', threading.current_thread().name)

        time.sleep(0.2)
    except Exception:
        q.put(sys.exc_info())


def b(x):
    ''''''
    try:
        # for i in range(5):
        print('Program b(' + x + ') is running... at ', ctime(), u'.线程名为：', threading.current_thread().name)
        time.sleep(0.1)
    except Exception:
        q.put(sys.exc_info())


if __name__ == '__main__':
    q = queue.Queue()
    print('Mainthread %s is running...' % threading.current_thread().name)
    thread_list = []
    for i in range(400):  # 同时运行多个
        t1 = threading.Thread(target=a)
        thread_list.append(t1)

    t2 = threading.Thread(target=b, args=('Python', ))
    thread_list.append(t2)
    t3 = threading.Thread(target=b, args=('Java', ))
    thread_list.append(t3)

    for t in thread_list:
        t.setDaemon(True)  # 设置为守护线程，不会因主线程结束而中断
        t.start()
    for t in thread_list:
        t.join()  # 子线程全部加入，主线程等所有子线程运行完毕

    # 捕获子线程异常;主要通过返回的堆栈为空代表正常
    if q.empty():
        if threading.active_count() == 1:
            print('main success')
    else:
        print(q.get())
        raise Exception(u'main error')

    print('Mainthread %s ended.' % threading.current_thread().name)
