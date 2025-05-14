#   variavel lista é uma variavel provisoria que sera apagada apos ser convertida em tupla.
lista = list()
continuar = 's'

#   loop infinito para a interacao onde só sai do loop digitando o "n".
while True:

    if continuar == 's':
        lista.append(int(input('digite um numero: ')))
        continuar = str(input('deseja continuar[s/n]: '))

    elif continuar == 'n':
        print('obrigado')
        break
    else:
        print('opcao invalida\ntente novamente')
        continuar = str(input('deseja continuar[s/n]: '))

# variavel tupla recebe valor de lista e depois a variavel lista é apagada.
tupla = tuple(lista)
del lista

print(f'valor: {tupla}')
print(f'o numero 9 apareceu {tupla.count(9)} vezes')
print(f'o numero 3 apareceu na posicao: {tupla.index(3)}')
print(f'os numeros pares sao: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=', ')
