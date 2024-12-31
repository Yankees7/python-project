from random import randint, choice


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def exam():
    '出题做答'
    funcs = {'+': add, '-': sub}

    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排序

    # 随机取出加减号
    op = choice('+-')
    result = funcs[op](*nums)
    # 用户作答，判断对错
    prompt = f'{nums[0]} {op} {nums[1]} = '
    i = 0
    while i < 3:
        try:
            answer = int(input(prompt).strip())
        except:
            continue
        if result == answer:
            print('不错呦', prompt, result)
            break
        print('不对呦')
        i += 1
    else:
        print('算了结果告诉你', prompt, result)


def show_menu():
    while 1:
        exam()
        try:
            yn = input('继续吗(y/n)?').strip()[0]
        except IndexError:
            yn = 'y'
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in ['n', 'N']:
            print('\nBye-bye')
            break


if __name__ == '__main__':
    show_menu()
