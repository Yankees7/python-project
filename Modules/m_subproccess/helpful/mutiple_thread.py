import sys
import concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":
    """控制线程数量"""
    # 创建线程池，最大容量10个;ThreadPoolExecutor(max_workers=4, thread_name_prefix='test_')
    pool = ThreadPoolExecutor(10)
    # 往线程池里提交线程并执行
    for i in all_list:
      pool.submit(func, func_arg1, func_arg2, str(i)) # i是第三个参数
    # 等待所有任务完成再关闭线程池pool.shutdown(wait=True)
    pool.shutdown(wait=True)
    print("所有线程执行完毕")
