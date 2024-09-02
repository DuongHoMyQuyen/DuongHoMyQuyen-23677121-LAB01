# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:52:45 2024

@author: Windows
"""

import math
a= float(input("So thuc a:"))
b= float(input("So thuc b:"))
x=((a+b)/(pow(a,1/3)+pow(b,1/3)))/((pow(a,1/3)-pow(b,1/3)))**2
print("ket qua:",x)