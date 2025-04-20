# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:38:43 2022

Ex_02.03

@author: luanh
"""
base = 1
h = 0
cont = int(input("Digite até quando será divido: "))
if cont < 0:
    print("Valor inválido, fim do programa.")
else:
    while base <= cont:
        h = h + 1 / base
        base += 1
    print("O valor de H é %.2f" % h)