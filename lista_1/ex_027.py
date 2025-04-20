# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:11:08 2022

Ex_027 - Lista 1

@author: luanh
"""
A = float(input("Digite o 1º lado do triângulo: "))
B = float(input("Digite o 2º lado do triângulo: "))
C = float(input("Digite o 3º lado do triângulo: "))
if (A >= B + C) or (B >= A + C) or (C >= B + A):
    print("Não é possível formar um triângulo.")
else:
    if A == B and B == C:
        print("Este triângulo é equilátero.")
    else:
        if (A != B) and (B != C) and (A != C):
            print("Este triângulo é escaleno.")
        else:
            print("Este triângulo é isósceles.")