valor = float(input('digite o valor do produto R$ '))
desc = valor * 0.05
print('o valor do produto é de R$ {:.2f} e teve desconto de 5% ficando'
      'o valor final de R$ {:.2f}'.format(valor, valor - (valor * 0.05)))
print('o valor com desconto é de R$ {:.2f}'.format(valor - desc))