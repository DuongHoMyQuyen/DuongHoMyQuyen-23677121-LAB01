# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:04:32 2024

@author: Windows
"""

a1=int(input("gio1:"))
a2=int(input("gio2:"))
b1=int(input("phut1:"))
b2=int(input("phut2:"))
c1=int(input("giay1:"))
c2=int(input("giay2:"))
if a1>24 and b1>60 and c1>60:
    print("Thoi gian khong hop le.")
if a2>24 and b2>60 and c2>60:
    print("Thoi gian khong hop le.")
thoigianbanggiay1= a1*3600 + b1*60 + c1
thoigianbanggiay2= a2*3600 + b2*60 + c1
tongthoigiantinhbanggiay= thoigianbanggiay1 + thoigianbanggiay2
hieuthoigiantinhbanggiay= thoigianbanggiay2 - thoigianbanggiay1
print("Tong thoi gian 2 gio:", tongthoigiantinhbanggiay)
print("Hieu thoi gian 2 gio:", hieuthoigiantinhbanggiay)