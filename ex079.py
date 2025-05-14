lista = []

lista.append(int(input('digite um numero: ')))

while True:

    continuar = ''
    continuar = str(input('deseja continuar [ S/N ]')).lower()

    if continuar == 'n':
        break
    if continuar == 's':
        num = int(input('digite outro numero: '))
        if num not in lista:
            lista.append(num)
        else:
            print('valor ja digitado')
        #lista.append(int(input('digite outro numero: ')))

    else:
        print('\ndigitou errado. tente novamente\n')

lista.sort()
print(f'a lista recebeu os seguintes numeros: {lista}')

