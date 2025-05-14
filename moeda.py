def metade(valor):
    met = valor / 2
    return met


def dobro(valor):
    dobrar = valor * 2
    return dobrar


def aumentar(valor):
    aumenta = valor * 1.1
    return aumenta


def diminuir(valor):
    diminui = valor * 0.9
    return diminui


quantia = float(input('digite um valor: '))

media = metade(quantia)
dobrar = dobro(quantia)
aumentar = aumentar(quantia)
diminuir = diminuir(quantia)

