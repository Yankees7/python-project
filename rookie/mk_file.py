import subprocess


def create_file(f_name):
    while 1:
        result = subprocess.run(f'ls {f_name}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not result.stderr:
            f_name = input('文件以存在，重新输入文件名')
        else:
            break

    print('请按照每行输入数据，输入end结束')
    l = []
    while 1:
        l1 = input('<输入end,结束>：').strip()
        if l1 == 'end':
            break
        else:
            l.append(l1)
    print(l)
    f = open(f_name, 'w')
    f.writelines(l + '\n')
    f.close()


if __name__ == '__main__':
    f_name = input('请输入文件名：')
    create_file(f_name)
