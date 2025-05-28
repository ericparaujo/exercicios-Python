def maior(*num):
    print(f'=' * 40)

    print(f'os valores passados foram: ', end=' ')
    for c in num:
        print(f'{c}', end=' ')
    print(f'totalizando {len(num)} numeros')
    print(f'o maior é {max(num)}')


maior(1, 2, 3, 9, 4, 5)
maior(1, 5, 2)
