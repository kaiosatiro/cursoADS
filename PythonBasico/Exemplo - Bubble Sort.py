import random


def aleatoria(n, inicio, fim):
    lista = []
    for i in range(n):
        lista.append(random.randint(inicio, fim))
    return lista


def troca(s, i, j):
    s[i], s[j] = s[j], s[i]


def empurra(s, n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)
#    i = 0
#    while i < n-1:
#        if s[i] < s[i+1]: #Ordenação decrescente
#            troca(s, i, i+1)
#        i += 1


def bubble_sort(s):
    n = len(s)
    while n > 1:
        empurra(s, n)
        n -= 1
#    for n in range(len(s), 1, -1):
#        empurra(s, n)


def bubble_sort2(s):
    s = s[:]
    n = len(s)
    while n > 1:
        empurra(s, n)
        n -= 1
    return s


lista = [50, 30, 40, 10, 20, 5, 0]
print(lista)
print(bubble_sort2(lista))
print(lista)
