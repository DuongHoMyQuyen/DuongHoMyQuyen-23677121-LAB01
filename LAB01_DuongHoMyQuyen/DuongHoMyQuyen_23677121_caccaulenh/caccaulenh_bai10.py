# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:40:23 2024

@author: Windows
"""

so_xe= input("So xe (gom 5 chu so):")
if len(so_xe) == 5 and so_xe.isdigit():
    so_nut = len(so_xe)
    print(f"Số xe của bạn có {so_nut} nút.")
else:
    print("Số xe không hợp lệ. Vui lòng nhập một số xe gồm 5 chữ số.")
