def leiaInt(a):
    a = str(input(a)).strip()
    if a.isnumeric():
        a = int(a)
        return a
    else:
        while True:
            print(f'ERRO')
            a = str(input(f'Digite um numero: {a}')).strip()
            if a.isnumeric():
                a = int(a)
                break
        return a


n = leiaInt('Digite um numero: ')
print(f'voce digitou o numero: {n}')
