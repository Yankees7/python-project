stack = []


def push_stack():
    data = input('请输入数据：').strip()
    if len(data) == 0:
        print('没有获取到数据')
    else:
        stack.append(data)


def pop_stack():
    if len(stack) == 0:
        print('栈已经为空')
    else:
        data = stack.pop()
        print(f'从栈中弹出来了：{data}')


def view_stack():
    print(stack)


def show_menu():
    prompt = '''(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): '''
    all_ch = ['0', '1', '2', '3']

    while 1:
        slt = input(prompt).strip()
        if slt not in all_ch:
            print('无效输入，请重试')
            continue
        if slt == '3':
            print('Bye bye!')
            break
        if slt == '0':
            push_stack()
        elif slt == '1':
            pop_stack()
        else:
            view_stack()


if __name__ == '__main__':
    show_menu()
