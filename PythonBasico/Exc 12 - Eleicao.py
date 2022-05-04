def eleicao():
    corona=0
    h1n1=0
    valido=[12, 15]
    invalido=[0, 99]
    branco=0
    nulo=0
    validos=0
    invalidos=0
    vencedor=0
    flag=True
    while flag:
        voto=int(int(input('Numero do candidato: ')))
        if voto in valido:
            validos+=1
            if voto == 12:
                corona+=1
            else:
                h1n1+=1
        elif voto in invalido:
            invalidos+=1
            if voto == 0:
                branco+=1
            else:
                nulo+=1
        flag=input('Para votar novamente aperte "s": ')
        if flag == 's':
            flag=True
        else:
            flag=False
            if corona > h1n1:
                vencedor=(f'Corona {corona} Votos')
            elif h1n1 > corona:
                vencedor=(f'H1N1  {h1n1} Votos')
            else:
                vencedor='EMPATE'
    return (f'Votos validos: {validos}\n'
            f'-- Corona: {corona}\n'
            f'-- H1N1: {h1n1}\n'
            f'Votos invalidos: {invalidos}\n'
            f'-- Brancos: {branco}\n'
            f'-- Nulos: {nulo}\n'
            f'**********************\n'
            f'- VECEDOR: {vencedor}')

X=eleicao()
print(X)
