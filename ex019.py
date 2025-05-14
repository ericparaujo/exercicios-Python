import random
al01 = str(input('digite o nome do primeiro aluno: '))
al02 = str(input('digite o nome do segundo aluno: '))
al03 = str(input('digite o nome do terceiro aluno: '))
al04 = str(input('digite o nome do quarto aluno: '))
lista = [al01, al02, al03, al04]

print('o aluno escolhido foi: {}'.format(random.choice(lista)))
