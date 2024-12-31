def get_info(name, age):
    if not 0 < age < 200:
        raise ValueError('年龄超出范围（1-119）')
    print(f'{name} {age}岁了')


def get_info2(name, age):
    assert 0 < age < 200, '年龄超出范围（1-119）'
    print(f'{name} {age}岁了')


if __name__ == '__main__':
    get_info('牛老师', 20)
    get_info2('凯歌', 230)
