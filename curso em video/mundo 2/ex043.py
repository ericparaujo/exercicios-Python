peso = float(input('qual é seu peso? '))
altura = float(input('qual a sua altura? '))

imc = peso / (altura ** 2)

# tabela
'''RESULTADO	SITUAÇÃO
Abaixo de 17	Muito abaixo do peso
Entre 17 e 18,49	Abaixo do peso
Entre 18,5 e 24,99	Peso normal
Entre 25 e 29,99	Acima do peso
Entre 30 e 34,99	Obesidade I
Entre 35 e 39,99	Obesidade II (severa)
Acima de 40	Obesidade III (mórbida)'''

cores = {
    'limpar':   '\033[m',
    'preto':    '\033[30m',
    'vermelho': '\033[31m',
    'verde':    '\033[32m',
    'amarelo':  '\033[33m',
    'azul':     '\033[34m',
    'magenta':  '\033[35m',
    'ciano':    '\033[36m',
    'cinza':    '\033[37m',
    'branco':   '\033[97m'
}

fundos = {
    'limpar':    '\033[m',
    'preto':     '\033[40m',
    'vermelho':  '\033[41m',
    'verde' :    '\033[42m',
    'amarelo':   '\033[43m',
    'azul':      '\033[44m',
    'magenta':   '\033[45m',
    'ciano':     '\033[46m',
    'cinza':     '\033[47m',
    'branco':    '\033[107m',
}

estilo = {
    'sem':'\033[0m',
    'negrito':'\033[1m',
    'sublinhado':'\033[4m',
    'negativo':'\033[7m',
}


print('seu indice de massa corporal (IMC) é de {:.2f}, '.format(imc), end='')

if imc < 17:
    print('{} esta muito abaixo do peso'.format(cores['vermelho']))
elif imc <= 18.49:
    print('esta abaixo do peso')
elif imc <= 24.99:
    print('esta normal')
elif imc <= 29.99:
    print('esta acima do peso')
elif imc <= 34.99:
    print('esta com OBESIDADE NIVEL I')
elif imc <= 39.99:
    print('esta com obesidade nivel II (severa)')
else:
    print('esta com OBESIDADE III (mórbida)')
