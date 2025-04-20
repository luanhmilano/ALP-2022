# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:01:42 2022

ex_02.04

@author: luanh
"""
cont = 1
senha = int(input("Jogador 1: Digite a senha: "))
if (senha < 0) or (senha > 100):
    print("Senha inválida.")
else: 
    while cont <= 5:
        tent = int(input(f"Jogador 2: Digite a {cont}° tentativa: "))
        if tent > senha:
            print("Um pouco menos.")
            cont += 1
        elif tent < senha:
            print("Um pouco mais.")
            cont += 1
        elif tent == senha:
            print("Parabéns! Você acertou.")
            print(f"A senha era {senha}")
            cont += 10
if cont == 6:
    print("Game Over.")
    print(f"A senha era {senha}.")
