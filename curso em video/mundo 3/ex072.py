contador = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
            'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove',
            'Vinte')

while True:
    escolha = int(input('digite um numero entre 0 e 20: '))
    if 0 <= escolha <= 20:
        ler = contador[escolha]
        print(f'{ler}')
        break
    else:
        print('opcao invalida\n\ntente novamente')