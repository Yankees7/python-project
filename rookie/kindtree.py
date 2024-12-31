import os

dir = '/tmp/mydemo'

l = os.listdir(dir)

print(f'{dir}:')
for i in l:
    print(i, '', end='')
print('\n')

n = 0
for i in l:
    if os.path.isdir(os.path.join(dir,i)):
        n += 1

for j in range(n):
    dir1 = os.path.join(dir, l[j])
    l1 = os.listdir(dir1)

    print(f'{dir1}:')
    for i in l1:
        print(i, '', end='')
    print('\n')
