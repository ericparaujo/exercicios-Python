def aumentar(valor, taxa):
    aumento = valor + (valor * (taxa / 100))
    return aumento


def diminuir(valor, taxa):
    reducao = valor - (valor * (taxa / 100))
    return reducao


def dobrar(valor):
    dobra = valor * 2
    return dobra


def metade(valor):
    met = valor / 2
    return met
