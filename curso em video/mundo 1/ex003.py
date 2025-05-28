num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))

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

num3 = num1 + num2
print(type(num3))
print("a soma dos valores {}{}{} e {}{}{} deu: {}{}{}" .format(cores['vermelho'], num1, cores['limpar'],
                                                               cores['vermelho'], num2, cores['limpar'],
                                                               estilo['negativo'], num3, cores['limpar']))
