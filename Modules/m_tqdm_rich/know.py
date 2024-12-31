"""
进度条模块:tqdm学习
"""
from tqdm import tqdm, trange
import time

# for i in tqdm(range(100)):
#     time.sleep(0.1)

"""desc描述,unit单位"""
# for i in tqdm(range(100), desc="Traning", unit="epoch"):
#     time.sleep(0.1)

"""trange(100) = tqdm(range(100))"""
# for i in trange(100, desc="Traning", unit="epoch"):
#     time.sleep(0.1)

"""tqdm(iterator),里面跟迭代器就行"""
l1 = ["a", "b", "c", "d", "e", "f"]
for i in tqdm(l1):
    time.sleep(0.1)
