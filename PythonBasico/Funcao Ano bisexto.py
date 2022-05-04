def ano_bi(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    else:
        return False

ano = int(input('Ano: '))
X = ano_bi(ano)
print(X)