# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 09:08:09 2022

ex02_02

@author: luanh
"""
cpar = 0
v = []
for i in range(0, 20):
    x = int(input(f"{i+1}° valor: "))
    v.append(x)
for i in range(0, 20):
    print(v[i])
    if v[i] % 2 == 0:
        cpar += 1
print(f"Existem {cpar} números pares no vetor.")