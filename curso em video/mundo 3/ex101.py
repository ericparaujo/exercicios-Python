from datetime import date


def voto(data):
    if 18 > idade >= 16:
        texto = 'VOTO OPCIONAL'
    elif idade >= 64:
        texto = 'VOTO OPCIONAL'
    elif idade >= 18:
        texto = 'VOTO OBRIGATORIO'
    else:
        texto = 'VOTO NEGADO'

    return texto


ano = int(input('digite o ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano

msg = voto(idade)
print(f'voce tem {idade} anos: {msg}')
