# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:06:50 2022

Ex03_03

@author: luanh
"""
sl4 = 0
sc2 = 0
sdp = 0
sds = 0
sm = 0
m = []
for i in range(0, 5):
    linha = []
    for j in range(0, 5):
        x = int(input(f"Digite o valor da posição {[i+1]}{[j+1]}: "))
        linha.append(x)
    m += [linha]
print("Matriz original: ")
for i in range(0, 5):
    print()
    for j in range(0, 5):
      print(m[i][j], end=' ') 
      sm += m[i][j]
      if i == 3:
          sl4 += m[i][j]
      if j == 1:
          sc2 += m[i][j]
      if i == j:
          sdp += m[i][j]
      if i + j == 4:
          sds += m[i][j]
print()
print(f"Soma dos elementos da matriz: {sm}")
print(f"Soma dos elementos da linha 4: {sl4}")
print(f"Soma dos elementos da coluna 2: {sc2}")
print(f"Soma dos elementos da diagonal principal: {sdp}")
print(f"Soma dos elementos da diagonal secundária: {sds}")