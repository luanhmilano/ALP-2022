# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:48:14 2022
Ex_030
@author: luanh
"""
N1 = int(input("Digite um número inteiro: "))
N2 = int(input("Digite outro número inteiro: "))
if N1 == N2:
    print("%d é igual a %d." % (N1, N2))
else:
    if N1 > N2:
        print(f"{N1} é o maior número.")
        print(f"{N2} é o menor número.")
    else:
        print(f"{N2} é o maior número.")
        print(f"{N1} é o menor número.")
