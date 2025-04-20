# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 21:40:43 2022

Ex03_03

@author: luanh
"""
v = []
for i in range(0, 20):
    x = int(input(f"Digite um valor para a posição {[i+1]}: "))
    v.append(x)
print("Vetor com valores invertidos: ")
for i in range(19, -1, -1):
    print(v[i])