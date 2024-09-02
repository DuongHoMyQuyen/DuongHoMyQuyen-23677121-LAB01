# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:15:09 2024

@author: Windows
"""

can_nang= float(input("Can nang(kg):"))
chieu_cao= float(input("Chieu cao(m):"))
so_do_BMI= (can_nang/chieu_cao**2)
print(f"so_do_BMI: {so_do_BMI}")