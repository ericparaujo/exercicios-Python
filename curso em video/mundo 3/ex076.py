lista = ('lapis', 1.50,
         'borracha', 0.80,
         'caderno', 5.00,
         'estojo', 3.50,
         'transferidor', 2.50,
         'compasso', 3.50,
         'mochila', 250.00,
         'canetas', 20.00,
         'livro', 50.00)

print('----' * 10)
print('lista de material')
print('----' * 10)

for pos in range(0, len(lista)):
    if pos %2 == 0:
        print(f'{lista[pos]:.<30}', f'R${lista[(pos) + 1]:>10.2f}')

print('----' * 10)