expressao = str(input('digite uma expressao: '))
lista = []

for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('a expressao é valida')
else:
    print('a expressao é invalida')
