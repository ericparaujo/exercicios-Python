from datetime import date


def voto(nasc):
    idade = date.today().year - nasc

    if idade <= 15:
        resultado = 'voto negado'


    elif idade <= 18 or idade >= 65:
        resultado = 'voto opcional'

    else:
        resultado = 'voto obrigatorio'

    return resultado


nascimento = int(input('digite o ano de nascimento: '))
voto(nascimento)
print(date.today().year - nascimento)
print(voto(nascimento))
