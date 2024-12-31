import os

folder = '/tmp/mydemo'

for path, subpath, files in os.walk(folder):
    print(f'{path}:')
    for i in subpath:
        print(i, end=' ')
    for j in files:
        print(j, end=' ')
    print('\n')
