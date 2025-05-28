def voto(nasc):
    from datetime import date
    hoje = date.today().year
    idade = hoje - nasc

    if 18 > idade >= 16 or idade >= 65:
        return f'sua idade é {idade} : VOTO OPCIONAL'
    if idade >= 18:
        return f'sua idade é {idade}: VOTO OBRIGATORIO'
    else:
        return f'sua idade é {idade}: VOTO NEGADO'


nascimento = int(input('digite o ano de seu nascimento: '))
print(voto(nascimento))
