print('----------------------- \n \n ')
nome = str(input('digite seu nome completo: '))

print('em maiusculo: {}'.format(nome.upper()))
print('em minusculo: {}'.format(nome.lower()))
separado = nome.split()
junto = ''.join(separado)
print('o nome junto ficou: {}'.format(junto))
print('nome junto: {}'.format(''.join(separado)))
print('seu nome tem {} letras no total'.format(len(junto)))
print('seu nome tem {} letras no total'.format(junto.count('')))
print('o nome {} tem {} letras'.format(separado[0],separado[0].count('')))
