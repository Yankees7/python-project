import sys
import hashlib


def check_md5(fname):
    m = hashlib.md5()       #创建md5对象
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if data:
                break
            m.update(data)
    return m.hexdigest()


if __name__ == '__main__':
    md5 = check_md5(sys.argv[1])
    print(md5)
