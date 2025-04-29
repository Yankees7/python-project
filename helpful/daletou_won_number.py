import numpy as np

for i in range(5):
    print(np.random.choice(range(1, 35), 5, replace=False), np.random.choice(range(1, 11), 2, replace=False))
