lista = []
expressao = str(input('digite uma expressao: ')).lower()

lista = list(expressao)

abrir = lista.count('(')
fechar = lista. count(')')

if abrir == fechar:
    print(' sua expressao esta correta')
else:
    print('sua expressao esta errada')

print(lista)

print (abrir)
print(fechar)

