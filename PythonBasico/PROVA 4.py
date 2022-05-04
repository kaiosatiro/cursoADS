def troca(v, i , j):
    v[i], v[j] = v[j], v[i]

def empurra_maximo(v, n):
    for i in range(n-1):
        if v[i] > v[i+1]:
            troca(v, i, i+1)

def empurra_minimo(v, n):
    for i in range(n-1):
        if v[i] < v[i+1]:
            troca(v, i, i+1)

def bubble_sort(v, crescente=False):
    if crescente:
        empurra= empurra_maximo
    else:
        empurra= empurra_minimo
    
    for i in range(len(v), 1, -1):
        empurra(v, i)

v=[48,5,39,56,40,52]

bubble_sort(v, False)
print(v)