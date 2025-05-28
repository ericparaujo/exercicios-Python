lista_pessoas = []
lista_total = []
maior = menor = 0

while True:
    # for c in range(0, len(lista_pessoas) + 1):
    nome = str(input('Nome: ')).upper()
    peso = float(input('Peso: '))
    lista_pessoas.append(nome)
    lista_pessoas.append(peso)
    print(lista_pessoas)

    if len(lista_total) == 0:
        maior = menor = lista_pessoas[1]
    else:
        if lista_pessoas[1] > maior:
            maior = lista_pessoas[1]
        if lista_pessoas[1] < menor:
            menor = lista_pessoas[1]

    lista_total.append(lista_pessoas[:])
    lista_pessoas.clear()
    continuar = str(input('deseja continuar: [ S/N ]')).lower()

    if continuar == 'n':
        print(lista_total)
        print(f'foram cadastrados um total de {len(lista_total)}')
        print(f'maior: {maior} ', end=' ')

        for p in lista_total:
            if p[1] == maior:
                print(f'de {p[0]}')

        print(f'menor: {menor} ', end= ' ')

        for p in lista_total:
            if p[1] == menor:
                print(f'de {p[0]}')


        break

    elif continuar == 's':


        print('digite novamente')
