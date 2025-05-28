frase = str(input('digite uma frase: ')).strip().upper()
print('foram encontrados {} letras A'.format(frase.count('A')))
print('a primeira letra A é a {}° letra da frase'.format(frase.find('A')+1))
print('a ultima letra é a {}° letra da frase'.format(frase.rfind('A')+1))
