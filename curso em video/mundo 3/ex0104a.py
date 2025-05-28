def leiaInt(a):
    ok = False
    valor = 0
    while True:
        n = str(input(a))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO, tente novamnte.\033[m')

        if ok:
            break

    return valor


n = leiaInt('Digite um numero inteiro: ')
print(f'O numero digitado é {n}')