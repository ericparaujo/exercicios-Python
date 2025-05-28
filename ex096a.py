def area(larg, compr):
    m2 = larg * compr
    print(f'com a largura de {larg:.2f}m e comprimento de {compr:.2f}m é igual a {m2}m² de area')


print('===' * 20)
print('controle de terrenos\n')

l = float(input('digite a largura: '))
c = float(input('digite o comprimento: '))
area(l, c)
