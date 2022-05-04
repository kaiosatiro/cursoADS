def valor_estoque1(mercadorias):
    valor= 0
    for mercadoria in mercadorias:
        valor+= mercadoria[1] * mercadoria[2]
    return valor

def valor_estoque2(mercadorias):
    valor= 0
    for linha in range(len(mercadorias)):
        valor+= mercadorias[linha][1] * mercadorias[linha][2]
    return valor
    
def valor_estoque3(mercadorias):
    valor= 0
    for linha in range(len(mercadorias)):
        valor+= mercadorias[1] * mercadorias[2]
    return valor

mercadorias= [['notebook', 40, 5900.00], ['tablet', 10, 1800.00], ['smartphone', 35, 1299.50]]

X= valor_estoque2(mercadorias)
print(X)