def soma(L):
    impares= 0
    for i in range(len(L)):
        if L[i] % 2 != 0:
            impares+= L[i]
    return impares

lista= []
for i in range(10):
    x= int(input())
    lista.append(x)

print(f'A somaé: {soma(lista)}')