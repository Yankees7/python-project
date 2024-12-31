#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright Huawei Technologies Co., Ltd. 2010-2020. All rights reserved.
"""
二、对工作表中的行，列相关操作
"""

from openpyxl import load_workbook
from example import test_dir

if __name__ == "__main__":
    # 1.加载创建的工作簿
    wb = load_workbook(f"{test_dir}/新建工作簿.xlsx")
    # 2.读取工作表sheet1
    sh1 = wb["Sheet1"]

    # 3.在第一行之前插入一行
    sh1.insert_rows(1)
    # 在第三行之前，插入两行
    sh1.insert_rows(3, 2)

    # 4.删除第一行
    sh1.delete_rows(1)
    # 删除第二行及后面一行，共两行
    sh1.delete_rows(2, 2)

    # 5.在第三列前插入一列
    sh1.insert_cols(3)
    # 在第二列前插入两列
    sh1.insert_cols(2, 2)

    # 6.删除第五列
    sh1.delete_cols(5)
    # 删除第二列，及后面一列，共两列
    sh1.delete_cols(2, 2)

    #
    # 最后保存
    wb.save("新建工作簿.xlsx")
