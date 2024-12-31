import getpass

dic = {'tom': 123456, 'jerry': 1234}


def register():
    '用于注册'
    name = input('请输入用户：').strip()
    if len(name) == 0:
        print('用户名不能为空')
    elif dic.get(name):
        print('用户已存在')
    else:
        pwd = input('请输入密码：')
        dic[name] = pwd
        print('注册成功')


def login():
    '用于登陆'
    name = input('请输入用户：').strip()
    pwd = getpass.getpass('请输入密码：')
    if dic.get(name) == pwd:
        print('登陆成功')

    else:
        print('登陆失败')


def show_menu():
    prompt = '''(0) 注册
(1) 登陆
(2) 退出
清选择(0/1/2):'''
    funcs = {'0': register, '1': login}
    while 1:
        choice = input(prompt)
        if choice not in ['0', '1', '2']:
            print('输入错误请重新输入')
            continue
        if choice == '2':
            print('Bye bye')
            break
        funcs[choice]()


if __name__ == '__main__':
    show_menu()
