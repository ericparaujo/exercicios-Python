time = ('Palmeiras', 'Atlético Mineiro', 'Flamengo', 'Fortaleza', 'Bragantino', 'Athletico Paranaense',
        'Ceará', 'Fluminense', 'Atlético Goianiense', 'Bahia', 'Corinthians', 'Internacional', 'Santos',
        'Juventude', 'Sport Recife', 'Cuiabá', 'São Paulo', 'América Mineiro', 'Grêmio', 'Chapecoense')

print(f'os cinco primeiros colocados sao: {time[:5]}')
print(f'os quatro ultimos sao: {time[-4:]}')
print(f'em ordem alfabetica: {sorted(time)}')
print(f'o chapecoense ficou na posicao: {time.index("Chapecoense")}')
