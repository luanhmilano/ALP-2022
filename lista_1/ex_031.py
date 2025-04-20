# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:55:36 2022
Ex_031
@author: luanh
"""
N1 = int(input("Digite o 1° número: "))
N2 = int(input("Digite o 2° número: "))
N3 = int(input("Digite o 3° número: "))
if N1 > N2 and N1 > N3:
    if N2 > N3:
        print(f"A ordem crescente é: {N3} 4{N2} {N1}")
    else:
        print(f"A ordem crescente é: {N2} {N3} {N1}")
elif N2 > N1 and N2 > N3:
    if N1 > N3:
        print(f"A ordem crescente é: {N3} {N1} {N2}")
    else:
        print(f"A ordem crescente é: {N1} {N3} {N2}")
elif N3 > N1 and N3 > N2:
    if N1 > N2:
        print(f"A ordem crescente é: {N2} {N1} {N3}")
    else:
        print(f"A ordem crescente é: {N1} {N2} {N3}")