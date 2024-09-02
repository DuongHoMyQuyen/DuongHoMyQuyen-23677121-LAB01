# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:00:59 2024

@author: Windows
"""

print("26a: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Thu tu tang dan: ", a,b,c)
print("Bài 26b: ")
N = input("Nhap so nguyen: ")
dayso = "".join(sorted(N))
print("day so theo thu tu tang dan: ", dayso)