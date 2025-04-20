# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 15:16:11 2022

Ex04_01

@author: luanh
"""
matriz = []
vet = []
for i in range(6):
    linha = []
    for j in range(6):
        e = int(input(f"Digite o valor a ser adicionado {[i]}{[j]}: "))
        linha.append(e)
    matriz = matriz + [linha]
print(matriz)
n = int(input("Digite um número para multiplicar a matriz: "))
for i in range(6):
    for j in range(6):
        vet.append(n * matriz[i][j])
print(f"Vetor com a multiplicação: {vet}")