'''
studying
paramiko并不是内建模块,需要安装
paramiko,实现ssh客户端功能,也可以实现sftp功能
'''
import logging
import paramiko

logging.basicConfig(level=logging.INFO)
# 创建ssh客户端
ssh = paramiko.SSHClient()

# 设置自动接受服务器的主机秘钥
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 登录
ssh.connect('192.168.4.10', username='root', password='123', port=22)

# 执行命令,返回结果是长度为3的元组，这三项分别是：输入，输出和错误的类文件对象
result = ssh.exec_command('id root;id yangjing')
logging.info(len(result))

# 例如：
stdin, stdout, stderr = ssh.exec_command('id root;id yangjing')
logging.info(stdout.read().decode('utf8'))
logging.info(stderr.read().decode('utf8'))
