#!/usr/bin/env python3

print("Inserte un  úmero entre [0,997]")
print("(El máximo número de recursión es 997)")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

i = int(input())
print("El factorial del número que ingresó es:")
print(factorial(i))
