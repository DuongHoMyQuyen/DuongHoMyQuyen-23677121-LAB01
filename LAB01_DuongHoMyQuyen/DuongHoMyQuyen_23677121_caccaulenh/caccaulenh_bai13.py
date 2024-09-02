# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:42:42 2024

@author: Windows
"""

ngay=int(input("Ngày:"))
thang=int(input("Tháng:"))
nam=int(input("Năm:"))

print(f"Ngày/tháng/năm: {ngay}/{thang}/{nam}")

nam_2_so = nam % 100
print(f" Ngày/tháng/năm (rút gọn năm): {ngay}/{thang}/{nam_2_so}")

print(f" Năm/tháng/ngày: {nam}/{thang}/{ngay}")

print("\nNhập lại theo định dạng:")

input_a = input("Nhập theo định dạng ngày/tháng/năm: ")
ngay_a, thang_a, nam_a = map(int, input_a.split('/'))
print(f"Ngày: {ngay_a}, Tháng: {thang_a}, Năm: {nam_a}")

input_b = input("Nhập theo định dạng ngày/tháng/năm rút gọn: ")
ngay_b, thang_b, nam_b_2_so = map(int, input_b.split('/'))
nam_b = 2000 + nam_b_2_so if nam_b_2_so >= 0 else 1900 + nam_b_2_so
print(f"Ngày: {ngay_b}, Tháng: {thang_b}, Năm: {nam_b}")

input_c = input("Nhập theo định dạng năm/tháng/ngày: ")
nam_c, thang_c, ngay_c = map(int, input_c.split('/'))
print(f"Ngày: {ngay_c}, Tháng: {thang_c}, Năm: {nam_c}")