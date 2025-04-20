# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 14:29:39 2022

ex03_01

@author: luanh
"""
vet1 = []
vet2 = []
vetm = []
for i in range(0, 10):
    vet1.append(float(input(f"Digite as valores do primeiro vetor:{[i]} ")))
for i in range(0, 10):
    vet2.append(float(input(f"Digite os valores do segundo vetor: {[i]}: ")))
    vetm.append(vet1[i] * vet2[i])
print("1° vetor: ", vet1)
print("2° vetor: ", vet2)
print("Vetor com a multiplicação: ", vetm)
