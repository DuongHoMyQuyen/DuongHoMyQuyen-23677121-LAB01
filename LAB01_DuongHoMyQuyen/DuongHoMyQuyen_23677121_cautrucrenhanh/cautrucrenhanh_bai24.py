# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:43:57 2024

@author: Windows
"""

gio= int(input("Gio:"))
phut= int(input("Phut:"))
giay= int(input("Giay:"))
if gio<=24 and phut<=60 and giay<=60:
    print(f"Thoi gian:{gio} gio, {phut} phut, {giay} giay")
else:
    print("Thoi gian khong hop le.")
 