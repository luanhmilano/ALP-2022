# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:26:09 2022

Ex_02.02

@author: luanh
"""
cont = 1
while cont <= 10:
    num = float(input(f"Digite o {cont}° número: "))
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
print("O maior valor foi: ", maior)
print("O menor valor foi: ", menor)
