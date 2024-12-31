from random import randint


def func1(x):
    return x % 2


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result1 = filter(func1, nums)
    result2 = filter(lambda x: x % 2, nums)
    print(list(result1))
    print(list(result2))
