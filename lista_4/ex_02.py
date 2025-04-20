# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 09:39:25 2022

ex04_02

@author: luanh
"""
ca = 0
v = []
x = []
a = int(input("Digite o valor de A: "))
for i in range(0, 3):
    linhav = []
    linhax = []
    for j in range(0, 3):
        e = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linhav.append(e)
        linhax.append(0)
    v += [linhav]
    x += [linhax]
for i in range(0, 3):
    for j in range(0, 3):
        if v[i][j] != a:
            x[i][j] = v[i][j]
        else:
            x[i][j] = 'A'
            ca += 1
print("Matriz inicial: ")
for i in range(0, 3):
    print()
    for j in range(0, 3):
        print(v[i][j], end = ' ')
print()
print(f"Valores iguais a A na matriz: {ca}")
print("Matriz de elementos diferentes: ")
for i in range(0, 3):
    print()
    for j in range(0, 3):
        print(x[i][j], end = ' ')
