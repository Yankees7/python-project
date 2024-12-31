'''
studying
paramiko并不是内建模块,需要安装
paramiko,实现ssh客户端功能,也可以实现sftp功能
'''
import logging
import paramiko

logging.basicConfig(level=logging.INFO)


def batch_excu(user, passd, ipa, port, command):
    '''
    本函数批量机器执行命令
    '''
    try:
        # 创建ssh客户端
        ssh = paramiko.SSHClient()
        # 设置自动接受服务器的主机秘钥
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        # 登录
        ssh.connect(ipa, username=user, password=passd, port=port)
        # 执行命令,返回结果是长度为3的元组，这三项分别是：输入，输出和错误的类文件对象
        result = ssh.exec_command(command, timeout=5)
        # 打印标准输出和标准错误
        err_info = result[2].read().decode('utf8').strip()
        logging.info(result[1].read().decode('utf8').strip())
        # 如果存在标准错误，打印错误并归档error.log
        if err_info:
            logging.info(f'{err_info},{ipa}')
            with open('error.log', 'w', encoding='utf-8') as fo:
                fo.write(f'{err_info},{ipa}')
        ssh.close()
    except Exception as ssh_e:
        print(ssh_e)


if __name__ == "__main__":
    # paramiko在远程主机上执行命令的时候，命令的搜索路径为（/usr/local/bin:/bin:/usr/bin）
    # bash -l -c "somecmd" 这样才能读取到变量，目前测试仅限于系统变量/etc/bashrc定义变量，但--login好像不生效不读取profile里的所以不行
    # 由于paramiko读取path有限，不生效/etc/profile,所以如下执行
    command = "source /etc/profile;sed -i 's#<username>.*</username>#<username>p_artifact</username>#g' ${LCRP_HOME}/Settings.xml"
    with open('iplist.txt', encoding="utf-8") as fp:
        for i in fp:
            lis = i.split()
            ipa = lis[0]
            user = lis[1]
            passd = lis[2]
            port = lis[3]
            batch_excu(user, passd, ipa, port, command)
