# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:04:33 2022

Ex_02.01

@author: luanh
"""
cont = 0
num = 1
while num > 0:
    num = int(input("Digite um número positivo (um número negativo encerra o programa): "))
    if cont == 0:
        menor = num
    if num < 0:
        print("Valor negativo, fim do programa.")
        break
    elif num < menor:
        menor = num
    cont =+ 1
print("O menor valor digitado foi: ", menor)

