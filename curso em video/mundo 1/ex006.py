#      variaveis e formulas

numero = int(input('digite um numero: '))
dobro = (numero * 2)
triplo = (numero * 3)
raiz = (numero ** (1/2))

#     cores de fonte e de fundo

limpar = '\033[m'
cores = {
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
      'preto':    '\033[40m',
      'vermelho':   '\033[41m',
      'verde':     '\033[42m',
      'amarelo':   '\033[43m',
      'azul':      '\033[44m',
      'magenta':   '\033[45m',
      'ciano':     '\033[46m',
      'cinza':     '\033[47m',
      'branco':    '\033[107m'
}

negrito = '\033[1m'
sublinhado = '\033[4m'
negativo = '\033[7m'


print('Voce digitou: {}{}{}\n E o dobro é: {}{}{} \n O triplo é: {}{}{}\n E a raiz quadrada é: {}{}{}' .format(cores['amarelo'],   numero,   limpar,
                                                                                                               cores['vermelho'],  dobro,    limpar,
                                                                                                               cores['azul'],      triplo,   limpar,
                                                                                                               cores['verde'],     raiz,     limpar))
print(cores['magenta'], '__'*57, limpar)
print('| {}{} voce digitou o numero: {} e o dobro é: {}, o triplo é {}, o quadrado é: {} e a raiz quadrada é {:.2f} {}  |'.format(negrito, fundos['magenta'], numero, numero * 2, numero * 3, numero ** 2, numero **(1/2), limpar))
print(cores['magenta'], '--'*57, limpar)
