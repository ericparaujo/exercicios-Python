def fatorial(numero, a):
    fatorial = numero

    if a == True:

        for c in range(numero - 1, 0, -1):
            fatorial *= c
    else:
        return fatorial
    return fatorial


num = int(input('digite um valor: '))
show = bool(input('show?: '))
fatorial(num, show)

print(fatorial(num, show))
