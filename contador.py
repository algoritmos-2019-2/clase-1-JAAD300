#!/usr/bin/env python3
print("Precione un número entre [-x, 100]")
i = int(input())
print("Cuenta progresiva")
while i < 101:
    print(i)
    if i == 9:
        print("alto")
        break
    i += 1

