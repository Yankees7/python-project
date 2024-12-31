'''
这是一个python项目
'''

import getpass  # 123
import sys
import paramiko
import threading


def rcmd(ip, user, passwd, cmds):
    '远程执行命令，返回结果'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=user, password=passwd, port=22)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    print(stdout.read().decode(), f"\033[31;1m{stderr.read().decode()}\033[0m")


if __name__ == '__main__':
    '执行命令'
    ipfile = sys.argv[1]
    user = 'root'
    passwd = getpass.getpass()
    cmds = sys.argv[2]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=rcmd, args=(ip, user, passwd, cmds))
            t.start()
