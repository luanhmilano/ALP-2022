# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 13:17:17 2022

@author: luanh
"""
n200 = 0
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0
num = int(input("Digite um valor maior ou igual 200: "))
if num < 200:
    print("Valor inválido")
else:
        n200 = num // 200
        resto = num % 200
        n100 = resto // 100
        resto = resto % 100
        n50 = resto // 50
        resto = resto % 50
        n20 = resto // 20
        resto = resto % 20
        n10 = resto // 10
        resto = resto % 10
        n5 = resto // 5
        resto = resto % 5
        n2 = resto // 2
        resto = resto % 2
        n1 = resto
print(f"O total de cédulas de 200 é de: {n200}")
print(f"O total de cédulas de 100 é de: {n100}")
print(f"O total de cédulas de 50 é de: {n50}")
print(f"O total de cédulas de 20 é de: {n20}")
print(f"O total de cédulas de 10 é de: {n10}")
print(f"O total de cédulas de 5 é de: {n5}")
print(f"O total de cédulas de 2 é de: {n2}")
print(f"E um total de {n1} moeda(s).")