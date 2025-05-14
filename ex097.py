def escreva(mensagem):
    c = len(mensagem) + 4
    print('=' * c)
    print(f'{"":<2}{mensagem}{"":>2}')
    print('=' * c)


msg = str(input('digite algo: ')).strip()
escreva(msg)
