def fatorial(f, s):
    """help da função fatorial:
   função criada para fazer calculos fatoriais
   f = é onde o valor da valor da variavel "fator" sera armazenada
   s = é onde o valor se ira mostrar ou nao a formula na tela
   show ou true para mostrar
   nao digite nada para nao mostrar"""

    calculo = 1

    for c in range(f, 0, -1):
        calculo *= c
        if s:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')

    return calculo


fator = int(input('digite o numero a ser fatorado: '))
show = bool(input('show? '))
print(fatorial(fator, show))
help(fatorial)
