#!/usr/bin/env python3

def checador(n):
            for i in range(2, n):
                if (n % i) == 0:
                    return print(n, "no es primo")                                                                         
                else:
                    return print(n, "es primo")
print("ingrese número")
checador(int(input()))
