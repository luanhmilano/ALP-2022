# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:35:17 2022

Ex04_04

@author: luanh
"""
m = []
flag = 1
for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        x = int(input(f"Digite o valor da posição {[i+1]}{[j+1]}: "))
        linha.append(x)
    m.append(linha)
for i in range(0, 3):
    for j in range(0, 3):
        print(m[i][j], end=' ')
    print()
conti = 0
contj = 0
while flag == 1:
    total = 0
    if contj > 2:
        contj = 0
        conti += 1
        rep = m[conti][contj]
    else:
        rep = m[conti][contj]
        contj += 1
    for i in range(0, 3):
        for j in range(0, 3):
            if m[i][j] == rep:
                total += 1
    print(f"O valor de {[conti+1]}{[contj]} repete-se um total de: {total} vezes.")
    flag = int(input("Deseja ver o próximo valor? (1 para SIM, 2 para NÃO): "))
    while flag != 1 and flag != 2:
        flag = int(input("Digite 1 para SIM ou 2 para NÃO: "))