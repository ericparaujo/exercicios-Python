numero = int(input('digite qualquer numero: '))
somar1 = (numero + 1)
subt1 = (numero - 1)

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
    'branco':   '\033[97m',

}

fundos = {
    'limpar':   '\033[m',
    'preto':    '\033[40m',
    'vermelho': '\033[41m',
    'verde':    '\033[42m',
    'amarelo':  '\033[43m',
    'azul':     '\033[44m',
    'magenta':  '\033[45m',
    'ciano':    '\033[46m',
    'cinza':    '\033[47m',
    'branco':   '\033[107m',
}

print('o sucessor desse numero é: {}{}{}'.format(cores['amarelo'], somar1, cores['limpar']))
print('o antecessor desse numero é: {}{}{}'.format(cores['amarelo'], subt1, cores['limpar']))
print(cores['vermelho'],'_' * 50,cores['limpar'])
print('{}{}o numero digitado foi: {} entao o antecessor é: {} e o seu sucessor é: {}{}'
      .format(fundos['amarelo'], cores['preto'], numero, (numero - 1), (numero + 1), fundos['limpar']))
