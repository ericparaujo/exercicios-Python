palavras = ('pastel', 'sabonete', 'panela', 'piada', 'pernambuco', 'cachorro', 'tabuada', 'paraguai', 'esquecido')

for p in palavras:
    print(f'para a palavra {p} ')
    for letras in p:
        if letras in 'aeiou':
            print(f'temos as letras {letras}')

