# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:14:35 2022

ex_02.05

@author: luanh
"""
option = 'S'
while option == 'S' or option == 's':
    cont = 1
    senha = int(input("Jogador 1: Digite a senha: "))
    if (senha < 0) or (senha > 100):
        print("Senha inválida.")
    else:
        while cont <= 5:
            tent = int(input(f"Jogador 2: Digite a {cont}° tentativa: "))
            if (tent == senha + 1 and tent > senha) or (tent == senha - 1 and tent < senha):
                print("TÁ QUENTE!!")
                cont += 1
            elif tent > senha:
                print("Um pouco menos.")
                cont += 1
            elif tent < senha:
                print("Um pouco mais. ")
                cont += 1
            else:
                print("Você acertou a senha, parabéns.")
                cont += 10
        if cont == 6:
            print("Você perdeu, tente novamente depois.")
            print(f"A senha era {senha}")
    option = input("Tentar novamente?(S/N): ")