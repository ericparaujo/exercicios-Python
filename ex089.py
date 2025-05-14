nome = nota1 = nota2 = 0
cadastro = []
lista = []

while True:
    nome = str(input('nome: ')).upper()
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    cadastro.append(nome)
    cadastro.append(nota1)
    cadastro.append(nota2)
    lista.append(cadastro[:])
    continuar = str(input('deseja continuar: [S/N] ')).lower()

    if continuar == 'n':
        break

    elif continuar == 's':
        cadastro.clear()

    else:
        print('Opção errada. Tente novamente')
        cadastro.clear()


print('======' * 5)
print('N°     nome            media')
for i, p in enumerate(lista):
    media = (p[1] + p[2]) / 2

    print(f'{i:<7}{p[0][:]:<10}{media:>10}')
print('======' * 5)

while True:
    aluno = int(input('mostrar nota de qual aluno: '))

    if aluno == 999:
        print('FINALIZANDO ...')
        print('<<<< VOLTE SEMPRE >>>>')
        break

    elif aluno <= len(lista):
        print(f'as notas do aluno {lista[aluno][0]} sao: {lista[aluno][1]} e {lista[aluno][2]}')


    else:
        print('opcao invalida. tente novamente ')
