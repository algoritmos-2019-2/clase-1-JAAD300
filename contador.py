#!/usr/bin/env python3
print("Precione un número entre [x, 100]")
i = int(input())
print("Cuenta progresiva de x a 100")
while i < 101:
    print(i)
    if i == 101:
        print("alto")
        break
    i += 1

