# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:12:02 2022

Ex03_04

@author: luanh
"""
v = []
for i in range(0, 50):
    x = int(input(f"Digite o valor da posição {[i+1]}: "))
    v.append(x)
for i in range(0, 50):
    if v[i] >= 0:
        print(v[i], end=' ')

