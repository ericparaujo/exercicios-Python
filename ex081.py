lista=list()

while True:
    num = int(input('digite um numero: '))
    continuar = str(input('deseja continuar: [S / N] ')).lower()
    if continuar == 'n':
        lista.append(num)
        break
    if continuar == 's':
        lista.append(num)
        num = int(input('digite outro numero: '))

    else:
        print('opcao invalida, tente novamente')

lista.sort(reverse=True)

print(lista)
print(f'foram digitados {len(lista)} valores')

if lista.count(5) == True:
    print('o numero 5 esta dentro da lista')
else:
    print('Desculpe, nao encontrei o numero 5 na lista')
