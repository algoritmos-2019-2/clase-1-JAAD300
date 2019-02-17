#!/usr/bin/env python3

print("inserte un n úmero entre [0,20]")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

i = int(input())
print(factorial(i))
