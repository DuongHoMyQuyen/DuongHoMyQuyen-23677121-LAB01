# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:16:50 2024

@author: Windows
"""

a= float(input("nhap a:"))
b= float(input("nhap b:"))
if a==0:
    if b==0:
        print("Phuong trinh vo so nghiem.")
    else:
        print("Phuong trinh vo nghiem.")
else:
    x= -(b/a)
    print("Phuong trinh co nghiem duy nhat",x)