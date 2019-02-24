#!/usr/bin/env python3


print("inserte el primer término de la serie Fibo")

def fibo(n):
    if n == 0:
        return print("de a cuerdo!")
    else:
        return print("incio incorrecto")
    
i = int(input())

fibo(i)

def Fob(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


print(Fob(10000))




