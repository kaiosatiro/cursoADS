def aprovados(alunos):
    aprovados= []
    for i in alunos:
        cont= 0
        for x in alunos[i]:
            cont+= x
        media= cont / len(alunos[i])
        if media >= 6:
            aprovados.append(i)
    return aprovados

def incluir_nota(alunos, nome, nota):
    while True:
        try:
            alunos[nome].append(nota)
        except:
            alunos[nome]= []
            alunos[nome].append(nota)
        return alunos

def maiores_notas(alunos):
    maiores= {}
    for i in alunos:
        maiores[i]= max(alunos[i])
    return maiores

lista_alunos= {
    'José':[8,9,10], 'Maria':[4,5,6], 'João':[7,8,7], 'Adalberto':[5,6,4], 'Juscelino':[4,8,8]
}

print(incluir_nota(lista_alunos, 'João', 8))
print(incluir_nota(lista_alunos, 'José', 9))
print(incluir_nota(lista_alunos, 'Maria', 8))
print(incluir_nota(lista_alunos, 'Adalberto', 7))
print(incluir_nota(lista_alunos, 'Juscelino', 7))
print(incluir_nota(lista_alunos, 'Ribamar', 6.5))
print(incluir_nota(lista_alunos, 'Ribamar', 6))
print(incluir_nota(lista_alunos, 'Ribamar', 7))
print(incluir_nota(lista_alunos, 'Ribamar', 8))
