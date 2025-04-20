# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:53:57 2022

ex02_08

@author: luanh
"""
cont = 1
total = 0
while cont <= 3:
    sat = 0
    c = 0
    d = 0
    ac = 0
    ad = 0
    mov = 's'
    movt = 0
    ide = int(input("Digite o código do %d° cliente: " % cont))
    san = float(input("Digite o saldo do %d° cliente: " % cont))
    while mov != 'F' and mov != 'f':
        print("-------------------------------------")
        print("Qual movimentação foi realizada?: ")
        print("Digite C para crédito: ")
        print("Digite D para débito: ")
        print("Digite F para finalizar: ")
        mov = input()
        while mov !='F' and mov !='f' and mov !='C' and mov !='c' and mov !='D' and mov !='d':
            mov = input("Valor inválido, digite um dos códigos de movimentação: ")
        if mov == 'C' or mov == 'c':
            c = float(input("Qual o valor da movimentação(C)?: "))
            sat = (san - ad - ac) - c
            while (san - ad - ac) - c < -1000:
                sat = (san - ad - ac)
                print("Você não pode realizar essa movimentação.")
                c = float(input("Digite um novo valor ou digite 0: "))
            ac = ac + c
        elif mov == 'D' or mov == 'd':
            d = float(input("Qual o valor da movimentação(D)?: "))
            sat = (san - ad - ac) - d
            while (san - ad - ac) - c < -1000:
                sat = (san - ad - ac)
                print("Você não pode realizar essa movimentação.")
                d = float(input("Digite um novo valor ou digite 0: "))
            ad = ad + d
        else:
            movt = san - sat
            if movt == san:
                sat = san
                total = total + sat
            else:
                sat = san - movt
                total = total + sat
            if cont == 1:
                maior = sat
                cli = ide
            elif maior < sat:
                maior = sat
                cli = ide
    cont += 1
    print("Código do cliente: ", ide)
    print("Saldo anterior: ", san)
    print("Saldo atual: ", sat)
    print("-------------------------------------")
print("Total de dinheiro em caixa no banco: %.2fR$" % total)
print("Código do cliente com maior saldo: %d " % cli)
print("Saldo do cliente com maior saldo: %.2fR$" % maior)