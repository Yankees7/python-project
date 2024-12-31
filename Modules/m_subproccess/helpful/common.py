import sys
import os
import subprocess
import logging as log
import threading
import shutil


log.basicConfig(level=log.INFO)

class common:
    WORKSPACE = "/usr1/workspace"

    """补充: popen_obj.poll()返回码
    0 正常结束
    1 sleep
    2 子进程不存在
    5 kill
    None 在运行
    """
    @staticmethod
    def execute_command(cmd: str, workingdir: str=WORKSPACE) -> None:
        """执行系统命令"""
        log.info("Execute Command: %s", cmd)
        command = ["bash", "-c", cmd]
        if sys.platform == "win32":
            command = ["cmd", "/c", cmd]
        popen_obj = subprocess.Popen(command, cwd=workingdir, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while popen_obj.poll() is None:
            line = popen_obj.stdout.readline().strip()
            if line:
                log.info(line.decode("utf-8", "ignore"))
        if not popen_obj.returncode:
            log.info("Execute success about: %s:%s", workingdir, cmd)
        else:
            raise Exception("Command return code: %s",popen_obj.returncode)
    
    @staticmethod
    def copyto(src: str, dest: str) -> None:
        """拷贝包(文件)到目录"""
        if not os.path.exists(dest):
            os.makedirs(dest)
        for p in glob.glob(src):
            shutil.copy(p, dest)

    
if __name__ == "__main__":
    """多线程并发示例"""    
    # 创建线程列表
    thread_list = []
    for func in [fucn1, func2, func3]:
        t = threading.Thread(target=func, argv=(i,))
        thread_list.append(t)
    # 设置守护进程并开始执行
    for t in thread_list:
        t.setDaemon(True)
        t.start()
    # 主线程等待子线程结束
    for t in thread_list:
        t.join()
