# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:49:13 2024

@author: Windows
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

max_num = a

if b > max_num:
    max_num = b

if c > max_num:
    max_num = c

print("Số lớn nhất là:", max_num)
