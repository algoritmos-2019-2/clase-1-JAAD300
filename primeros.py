#!/usr/bin/env python3

print("ingrese un número")

def primero(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "no es primo")
                break
            else:
                print(n, "es primo")
            else:
                print(n, "no es primo")

primero(int(input())

