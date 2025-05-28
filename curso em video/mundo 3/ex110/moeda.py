def dobro(valor=0, formato=False):
    preco = valor * 2
    return preco if formato is False else moeda(preco)


def metade(valor=0, formato=False):
    preco = valor / 2
    return preco if formato is False else moeda(preco)


def aumento(valor=0, porcento_mais=0, formato=False):
    preco = valor + (valor * porcento_mais) / 100
    return preco if formato is False else moeda(preco)


def reducao(valor=0, porcento_menos=0, formato=False):
    preco = valor - (valor * porcento_menos) / 100
    return preco if formato is False else moeda(preco)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')



def resumo(valor, porcento_mais, porcento_menos):
    print('-_-_' * 10)
    print('RESUMO DO VALOR'.center(30))
    print('-_-_' * 10)
    print(f'o valor é: \t\tR${valor:.2f}')
    print(f'o dobro  é \t\t{dobro(valor, True)}')
    print(f'a metade é \t\t{metade(valor, True)}')
    print(f'{porcento_mais}%  é \t\t\t{aumento(valor, porcento_mais, True)}')
    print(f'{porcento_menos}% é \t\t\t{reducao(valor, porcento_menos, True)}')
