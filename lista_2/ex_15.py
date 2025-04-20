# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:30:29 2023
ex2_15
@author: luanh
"""
c = float(input("Digite o valor do capital inicial: "))
i = float(input("Digite o valor da taxa por trimestre: "))
x = int(input("Digite o total de anos da aplicação: "))
totaltri = x * 4
cont = 1
saldo = 0
saldotot = 0
while cont <= totaltri:
    m = c * ((1 + (i/100)) ** cont)
    saldo = (m - c) - saldotot
    print(f"{cont}° Trimestre: ")
    print(f"Montante: {m:.2f}")
    print(f"Saldo: {saldo:.2f}")
    cont += 1
    saldotot += saldo
    input()
print(f"Saldo total acumulado: {saldotot:.2f}")
