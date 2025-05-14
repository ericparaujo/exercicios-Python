print('_____' *10)
print(f'{"LOJA SUPER BARATAO":^50} ')
print('_____' * 10)

gasto = 0
produto1000 = 0
produto = ' '
menor_produto = ' '
total = 0

while True:

    continuar = ' '
    while continuar not in 'N':
        produto = str(input('nome do produto: ')).strip()
        preco = int(input('preço: '))

        if gasto == 0:
            gasto = preco
            menor_produto = produto
        if preco < gasto:
            gasto = preco
            menor_produto = produto
            total += preco
        if preco >=1000:




        continuar = str(input('deseja continuar: [S/N]')).strip().upper()

    if continuar == 'N':
        break

print(f'o produto mais barato foi{menor_produto}')
print(f'e custou: {gasto})
print(f'o total é de {total}')