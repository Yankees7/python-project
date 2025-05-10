# ！usr/bin/env python3
# -*- coding: utf-8 -*-
import random


def generate_lottery_numbers():
    # 前区号码：从 1 到 35 中随机选择 5 个不重复的号码
    front_area = sorted(random.sample(range(1, 36), 5))
    # 后区号码：从 1 到 12 中随机选择 2 个不重复的号码
    back_area = sorted(random.sample(range(1, 13), 2))
    return front_area, back_area


if __name__ == "__main__":
    print("生成的 5 组大乐透号码如下：")
    for i in range(5):
        front, back = generate_lottery_numbers()
        print(f"第 {i + 1} 组 - 前区号码: {front}, 后区号码: {back}")
