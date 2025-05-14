lista = list()

for c in range(0, 5):
    num = int(input('digite um numero: '))
    if c == 0:
        lista.append(num)

    if c > 0:
        if num > lista[-1]:

             lista.append(num)

        else:
            posicao = 0
            while posicao < len(lista):
                if num <= lista[posicao]:
                    lista.insert(posicao, num)
                    break
            posicao += 1


print(lista)