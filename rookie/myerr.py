try:
    num = int(input('number:'))
    result = 100 / num
except ValueError:
    print('必须输入非零整数')
except ZeroDivisionError:
    print('必须输入非零整数')
except KeyboardInterrupt:
    print('\nBye-bye')
except EOFError:
    print('\nBye-bye')
else:   # 不发生异常才执行的代码
    print(result)
finally:  # 不管异常是否发生，都会执行
    print('ok')
