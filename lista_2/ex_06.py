# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:51:13 2022

ex_02.06

@author: luanh
"""
cont = 1
distance = 0
litros = 0
while cont > 0:
    vel = int(input("Digite a velocidade do carro no trecho: "))
    peri = int(input("Digite o período de tempo em minutos: "))
    if vel <= 0 or peri <= 0:
        print("Valor de velocidade e/ou de tempo inválido.")
        cont = vel
    else:
        distance_trecho = vel * (peri / 60)
        litros_trecho = distance_trecho / 10
        distance = distance + distance_trecho
        cont = vel
        print("Distância no trecho: %.2f" % distance_trecho)
        print("Litros usados no percurso: %.2f" % litros_trecho)
litros = distance / 10
print("Distância da viagem: %.2f" % distance)
print("Total de litros usados: %.2f" % litros)