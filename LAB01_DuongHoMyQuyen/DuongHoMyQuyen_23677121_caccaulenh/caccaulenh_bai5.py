# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:49:31 2024

@author: Windows
"""

a=float(input("Giay:"))
b=float(input("Phut:"))
c=float(input("Gio:"))
tong_thoi_gian_tinh_bang_giay= ((a*3600)+(b*60)+c)
if c < 0 or b < 0 or a < 0 or b >= 60 or a >= 60 :
    print("Dinh dang khong hop le")
else:
    print("Tong thoi gian tinh bang giay:", tong_thoi_gian_tinh_bang_giay)
    