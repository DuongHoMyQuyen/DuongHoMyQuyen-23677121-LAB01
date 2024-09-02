# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:06:20 2024

@author: Windows
"""

chucai= input("Mot chu cai:")
if len(chucai) == 1 and chucai.islower():
    print("Mot chu cai in hoa:", chucai.upper())
if len(chucai) == 1 and chucai.isupper():
    print("Mot chu cai in thuong:", chucai.lower())