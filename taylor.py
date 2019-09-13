'''
taylor.py
'''
import math

def factorial (n):
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

def potencia (base, exp):
    res = 1
    for i in range(0, exp):
        res = res * base
    return res

def sen (deg):
    rad = (deg * math.pi) / 180
    sum = rad
    for i in range(2, 10):
        n = (2 * i) - 1
        # even
        if i % 2 == 0:
            sum = sum - potencia(rad, n) / factorial(n)
        # odd
        else:
            sum = sum + potencia(rad, n) / factorial(n)
    return sum

def main ():
    print(sen(3.1416/2))

if __name__ == "__main__":
    main()
