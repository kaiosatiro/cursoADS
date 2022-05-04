# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Caio Satiro          2020019
# ALUNO 2: Mirelly Simões       1903911
# ALUNO 3: Victor Ezemplari     2100264
# ALUNO 4: Carolina Aparecida   2100194
# ALUNO 5: Ricardo Tadeu        2101700
# ALUNO 6: Carlos Roberto       2020021


'''
Escreva uma função com o nome pertence, que recebe como argumentos de entrada
uma tupla e um item e retorna True, se o item estiver armazenado na tupla, e
False, caso contrário.
'''


def pertence(tupla, item):
    return item in tupla


'''
Escreva uma função chamada substituir que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):
    try:
        if velho not in lista:
            print('Item não encontrado na lista')
            raise ValueError
        else:
            for _ in range(len(lista) - 1):
                n = lista.index(velho)
                lista[n] = novo
    except ValueError:
        return lista

# def substituir(lista, velho, novo):
#     while velho in lista:
#         i = lista.index(velho)
#         lista[i] = novo
#     return lista

'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de entrada
uma lista e um item, e retorna uma lista contendo todos os índices em que o
item aparece na lista.
'''


def posicoes_lista(lista, item):
    lista_indice = []
    for i in range(len(lista)):
        if lista[i] == item:
            lista_indice.append(i)
    return lista_indice


'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada aprovados que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos aprovados
(um aluno é aprovado quando a média das suas notas é maior ou igual a 6).
'''


def aprovados(alunos):
    aprovados = []
    for i in alunos:
        cont = 0
        for x in alunos[i]:
            cont += x
        media = cont / len(alunos[i])
        if media >= 6:
            aprovados.append(i)
    return aprovados


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''


def incluir_nota(alunos, nome, nota):
    try:
        alunos[nome].append(nota)
    except KeyError:
        print('Aluno não encontrado!')
        if input('DESEJA inserir? (S/N): ').upper() == 'S':
            alunos[nome] = []
            alunos[nome].append(nota)
    finally:
        return alunos


# def incluir_nota(alunos, nome, nota):
#     alunos[nome].append(nota)
#     return alunos


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada maiores_notas que recebe como
argumentos de entrada o dicionário e retorna outro dicionário com o nome e a
maior nota de cada aluno.
'''


def maiores_notas(alunos):
    maiores = {}
    for i in alunos:
        maiores[i] = max(alunos[i])
    return maiores
