# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:38:44 2024

@author: Windows
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))

min_num = a

if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d

print("Số nhỏ nhất là:", min_num)
