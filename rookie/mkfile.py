import subprocess


def get_fname():
    '用于获取一个系统中不存在的文件名，它的返回值是一个文件名'
    while 1:
        fname = input('文件名：')
        result = subprocess.run(
            f'ls {fname}',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode != 0:
            break
        print('文件已存在，请重试')
    return fname


def get_content():
    '用于获取用户输入的多行文本，作为文件内容，它的返回值是列表'
    print('请输入文本内容，按行输入')
    content = []

    while 1:
        l1 = input('<input "end" to end>')
        if l1 != 'end':
            content.append(l1+'\n')
        else:
            break
    return content


def wfile(f_name, content):
    '把内容content写入到文件f_name中'
    with open(f_name, 'w') as f:
        f.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
