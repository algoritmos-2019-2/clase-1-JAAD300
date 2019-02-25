#!/usr/bin/env python3

def checador(n):
    l = n
    j = range(2, l)
    for i in j:
        if (i % i) != 0:
            return print(i, end="")
                                                                                    

print("ingrese número")
checador(int(input()))

