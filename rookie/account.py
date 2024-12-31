from time import strftime
import pickle
import os


def save(fname):
    date = strftime('%Y-%m-%d')
    # 输入存入金额和备注
    amount = int(input('金额：'))
    comment = input('备注：')
    # 从文件中取出 列表数据
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount
    # 向列表中追加一项
    line = [date, amount, 0, balance, comment]
    records.append(line)
    # 存盘
    with open(fname, 'rb') as fobj:
        pickle.dump(records, fobj)


def cost(fname):
    date = strftime('%Y-%m-%d')
    # 输入花费金额和备注
    amount = int(input('金额：'))
    comment = input('备注：')
    # 读取文件中 的列表数据
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount
    # 向列表中追加一项
    line = [date, amount, 0, balance, comment]
    records.append(line)
    # 存盘
    with open(fname, 'rb') as fobj:
        pickle.dump(records, fobj)


def query(fname):
    # 读取文件 列表数据
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    print(records)


def show_menu():
    prompt = '''(0)存钱
(1)取钱
(2)查询
(3)退出
请选择(0/1/2/3):'''
    funcs = {'0': save, '1': cost, '2': query}
    fname = "money.data"  # 定义用于记账的文件
    # 记账文件如果不存在，则初始化它
    if not os.path.exists(fname):
        # 采用列表存储每次的记录，每次的记录也是列表
        records = [[strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']]    # 初始记录
        with open(fname, 'wb') as fobj:
            pickle.dump(records, fobj)

    # 用户选择，对应调用函数
    while 1:
        choice = input(prompt).strip()

        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试')
            continue
        if choice == '3':
            print('Bye-bye')
            break
        funcs[choice](fname)


if __name__ == '__main__':
    show_menu()
