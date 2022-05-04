def primo1(n):
    divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False

def primo2(n):
    divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisores += 1
    return divisores == 2

def primo3(n):
    divisores = 0
    for i in range(2, n):
        if n % i == 0:
            divisores += 1
    return divisores == 0

def primo4(n):
    if n == 1: return False
    divisor = 2
    while n % divisor != 0:
        #print(f'{n} % {divisor} == {n % divisor}')
        divisor += 1
    #print(f'{n} % {divisor} == {n % divisor}')
    return divisor == n

def primo5(n):
    if n == 1: return False
    if n % 2 == 0: return n == 2
    divisor = 3
    while n % divisor != 0:
        divisor += 2
    return divisor == n

def primo6(n):
    if n % 2 == 0: return n == 2
    divisor = 3
    metade = n // 2
    while divisor <= metade and n % divisor != 0:
        divisor += 2
    return n > 1 and divisor > metade

from math import sqrt, ceil

def primo7(n):
    if n % 2 == 0: return n == 2
    divisor = 3
    raiz = ceil(sqrt(n))
    while divisor <= raiz and n % divisor != 0:
        divisor += 2
    return n > 1 and divisor > raiz