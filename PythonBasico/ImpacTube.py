#VERSAO LOGICA ENXUGADA
def recebe_canais(canais= []):
    n= int(input())
    for _ in range(n):
        canais.append(input().split(';'))
        
def converte_valores(lista):
    for i in lista:
        i[1], i[2] = int(i[1]), float(i[2])
        i[3] = i[3] == 'sim'

def calculo_bonus(lista, lista_bonus= []):
    for i in lista:
        if i[3]:
            lista_bonus.append([i[0], i[2] + b_premium* (i[1] // 1000)])
        else:
            lista_bonus.append([i[0], i[2] + b_comum* (i[1] // 1000)])
            
def exibe(lista):
    print('''-----
BÔNUS
-----''')
    for i in lista:
        print(f'{i[0]}: R$ {i[1]:.2f}')
        
canais= []
lista_bonus= []
recebe_canais(canais)
b_premium= float(input())
b_comum= float(input())
converte_valores(canais)
calculo_bonus(canais, lista_bonus)
exibe(lista_bonus)

# VERSAO ANTIGA
# def recebe_canais(canais= []):
#     n= int(input())
#     for _ in range(n):
#         canais.append(input().split(';')) 
# def converte_valores(lista):
#     for i in range(len(lista)):
#             lista[i][1],lista[i][2] = int(lista[i][1]), float(lista[i][2])
# def calculo_bonus(lista, lista_bonus= []):
#     for i in range(len(lista)):
#         if lista[i][3] == 'sim':
#             lista_bonus.append([lista[i][0], lista[i][2] + b_premium* (lista[i][1] // 1000)])
#         else:
#             lista_bonus.append([lista[i][0], lista[i][2] + b_comum* (lista[i][1] // 1000)])
# def exibe(lista):
#     print('''-----
# BÔNUS
# -----''')
#     for i in range(len(lista)):
#         print(f'{lista[i][0]}: R$ {lista[i][1]:.2f}')
# canais= []
# lista_bonus= []
# recebe_canais(canais)
# b_premium= float(input())
# b_comum= float(input())
# converte_valores(canais)
# calculo_bonus(canais, lista_bonus)
# exibe(lista_bonus)