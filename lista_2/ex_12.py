# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:53:36 2022

ex02_12

@author: luanh
"""
cont = 0
fib1 = 1
fib2 = 0
fib = 1
while cont < 20:
    print(fib)
    fib = fib1 + fib2
    fib2 = fib1
    fib1 = fib1 + 1
    cont += 1 