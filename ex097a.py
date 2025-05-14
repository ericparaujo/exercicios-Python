def escreva(t):
    print(f'{"x" * (len(t) + 4)}')
    print(f'{"":<2}{t}{"":<2}')
    print(f'{"x" * (len(t) + 4)}')

    return



texto = str(input('digite uma mensagem: ')).upper()

escreva(texto)
