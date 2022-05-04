def segunda_chance():
    n= int(input())
    original= []
    final= []
    alter= 0
    for _ in range(n):
        x= float(input())
        original.append(x)
    for i, item in enumerate(original):
        x= float(input())
        if original[i] == 10:
            final.append(original[i])
        elif x != 10:
            final.append(original[i])
        elif original[i] <= 8:
            final.append(original[i]+2)
            alter+= 1
        elif original[i] > 8:
            final.append(10)
            alter+= 1
    print(f'NOTAS ALTERADAS: {alter}')
    for i, item in enumerate(original):
        if item != final[i]:
            print(f'*({i+1:03}) original: {item:05.2f} | final: {final[i]:05.2f}')
        elif item == final[i]:
            print(f'-({i+1:03}) original: {item:05.2f} | final: {final[i]:05.2f}')

segunda_chance()