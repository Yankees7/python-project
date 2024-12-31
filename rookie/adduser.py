import sys
import subprocess
from string import ascii_letters, digits
from random import choice

all_ch = ascii_letters + digits


def mk_user(name, file):
    # 判断用户，并创建
    result = subprocess.run(
        f'id {name}',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if result.returncode == 0:
        print(f'{name} 已存在')
        exit(1)
    else:
        subprocess.run(
            f'useradd {name}',
            shell=True
        )

    # 随机密码并加密码
    pwd = ''
    for i in range(8):
        ch = choice(all_ch)
        pwd += ch
    subprocess.run(
        f'echo {pwd} | passwd --stdin {name}',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # 追加写入文件
    with open(file, 'a') as f:
        f.write(f'{sys.argv[1]}:{pwd}' + '\n')


if __name__ == '__main__':
    mk_user(sys.argv[1], sys.argv[2])
