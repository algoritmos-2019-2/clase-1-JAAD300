#!/usr/bin/env python3


def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n-1)
print("inserte número de [1, 999]")
print("(el número máximo de recursión es 998)")
i = int(input())
print("la suma del 1 hasta el número que escribió es:")
print(suma(i))
