#!/usr/bin/env python3

def checador(n):
    if n > 1:

        for i in range(2,n):
             if (n % i) == 0:
                  print(n,"is not a prime number")
        break
    else:
            print(n,"is a prime number")
    


print("inserte un número")


checador(int(input())



