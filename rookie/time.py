import time

st = time.time()
result = 0
for i in range(20000000):
    result += i

ed = time.time()

t = ed - st
print(result, f'{t:.2}')
