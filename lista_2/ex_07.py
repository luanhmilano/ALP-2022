# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:04:11 2022

ex02_07

@author: luanh
"""
cont = 1;
tir = 0;
isentos = 0;
while cont <= 10:
    nome = input("Digite o nome do %d° contribuinte: " % cont);
    cic = input("Digite o CIC do %d° contribuinte: " % cont);
    rb = float(input("Digite a renda bruta do %d° contribuinte: " % cont));
    dep = int(input("Digite o número de dependentes do %d° contribuinte: " % cont));
    print()
    if rb < 0:
        print("Valor de renda bruta inválido.");
        cont += 10;
    elif dep < 0:
        print("Valor de dependentes inválido.");
        cont += 10;
    elif len(cic) != 11:
        print("Valor do CIC inválido.");
        cont += 10;
    else:
        rl = rb - (dep * 600);
        if rl <= 1000:
            ir = 0;
            isentos += 1;
        elif rl > 1000 and rl <= 5000:
            ir = rl * (15/100);
            tir = tir + ir;
        else:
            ir = rl * (25/100);
            tir = tir + ir;
        print("Nome: ", nome);
        print("CIC: ",cic[0:3],'.',cic[3:6],'.', cic[6:9],'-', cic[9:11]);
        print("Total pago de imposto: ", ir)
        print()
        cont += 1;
print("Total arrecadado pela receita: ", tir);
print("Total de contribuintes isentos: ", isentos);