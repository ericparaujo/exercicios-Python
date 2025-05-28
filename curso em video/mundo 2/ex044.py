compras = float(input('Qual o preço das compras? '))

print('FORMAS DE PAGAMENTOS:')
print('[ 1 ] A vista no dinheiro')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2 X no cartão')
print('[ 4 ] 3 ou mais no cartão')

formas = float(input('qual é a opção? '))

if formas == 1:
    pg = compras - (compras * 0.1)
    print('o valor de R${:.2f} no dinheiro teve 10% de desconto e o valor final é de R${:.2f} '.format(compras, pg))
elif formas == 2:
    pg = compras - (compras * 0.05)
    print('o valor de R${:.2f} no cartao teve desconto de 5% e o valor final é de R${:.2f}'.format(compras, pg))
elif formas == 3:
    pg = compras // 2
    print('o valor de R${:.2f} parcelado em 2 x no cartao ficou em R${:.2f} em cada parcela'.format(compras, pg))
elif formas == 4:
    parcelas = float(input('digite a quantidade de parcelas: '))
    pg = compras + (compras * 0.2)
    if parcelas >=3:
        print('o valor de R${:.2f} parcelado em {:.0f} vezes no valor de R${:.2f} e no total saira a R${:.2f}'
              .format(compras, parcelas, pg // parcelas, pg))
    else:
        print('o valor de R${:.2f} parcelado em 2 x no cartao ficou em R${:.2f} em cada parcela1'.format(compras, pg // 2))
else:
    print('voce escolheu uma opcao inexistente, tente novamente')
