import logging

# 读行方法来遍历
# readline读行（包括\n），返回字符串
if __name__ == "__main__":
    with open('iplist.txt', encoding="utf-8") as fp:
        line = fp.readline()
        while line:
            lis = line.split()
            x = lis[0]
            print(x)
            line = fp.readline()

# for来遍历
if __name__ == "__main__":
    with open('iplist.txt', encoding="utf-8") as fp:
        for i in fp:
            lis = i.split()
            ipa1 = lis[0]
            user1 = lis[1]
            passd1 = lis[2]
            port1 = lis[3]
