lista = []
media = idade = 0

while True:

    dicionario = {}

    dicionario['nome'] = str(input('nome: ')).upper().strip()

    while True:
        dicionario['sexo'] = str(input('sexo: [M/F] ')).upper()[0].strip()
        if dicionario['sexo'] in 'MF':
            break
        else:
            print('\nsexo errado, tente novamente\n')

    dicionario['idade'] = int(input('idade: '))
    idade += dicionario['idade']
    lista.append(dicionario.copy())

    while True:
        continuar = str(input('deseja continuar: [S/N] ')).lower().strip()
        if continuar in 'ns':
            break

        else:
            print('respoda apenas [ S ou N )')
            #continuar = str(input('deseja continuar: [S/N] ')).lower().strip()

    if continuar in 'n':
        break

media = idade / len(lista)
print(f'foram cadastrados {len(lista)} pessoas')
print(f'media de idade: {media} anos')

print(f'pessoas do sexo feminino: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p['nome']}, ', end='')
print()

print(f'as nomes com idades acima da media é: ', end='')
for p in lista:
    if p['idade'] >= media:
        print(f'{p['nome']}, ', end='')

