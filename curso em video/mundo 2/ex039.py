'''nascimento = int(input('Em que ano voce nasceu: '))

print(' voce tem {} anos'.format(2023 - nascimento))
if 2023 - nascimento > 19:
    print('devia ter se alistado em {}'.format(nascimento + 18))
elif 2023 - nascimento < 18:
    print ('voce devera se alistar daki a {} anos'.format(18 -(2023 - nascimento)))
else:
    print ('voce esta em periodo de alistamento, procure a junta militar de sua regiao')'''

from datetime import date
atual = date.today().year
nasc = int(input('digite o ano em que nasceu: '))
idade = atual - nasc

print('estamos no ano de {} e voce nasceu em {} com isso, sua idade é de {} anos'.format(atual, nasc, idade))

if idade == 18:
    print('voce ja pode se alistar, procure IMEDIATAMENTE a junta militar de sua cidade')
elif idade < 18:
    print('falta {} ano(s) para voce se alistar'.format(18 - idade))
else:
    print('voce devia ter se alistado a {} anos atras'.format(idade - 18))
