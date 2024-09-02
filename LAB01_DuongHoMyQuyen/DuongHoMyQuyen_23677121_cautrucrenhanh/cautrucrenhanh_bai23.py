# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:23:14 2024

@author: Windows
"""
import math
a= float(input("Nhap a:"))
b= float(input("Nhap b:"))
c= float(input("Nhap c:"))
delta= (b**2) - (4*a*c)
if delta >0:
    x1= -b + math.sqrt(delta)/ 2*a
    x2= -b - math.sqrt(delta)/ 2*a
    print("Phuong trinh co 2 nghiem phan biet:", x1, x2)
elif delta <0:
    print("Phuong trinh vo nghiem.")
elif delta ==0:
    print("Phuong trinh co nghiem kep.", x1=x2)