# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:53:37 2024

@author: Windows
"""

ky_tu_chu_thuong= input("Nhap chu thuong:")
if len(ky_tu_chu_thuong) == 1 and ky_tu_chu_thuong.islower():
    ky_tu_chu_hoa = ky_tu_chu_thuong.upper()
    print(f"Ký tự chữ hoa tương ứng là: {ky_tu_chu_hoa}")
else:
    print("Vui lòng nhập một ký tự chữ thường.")