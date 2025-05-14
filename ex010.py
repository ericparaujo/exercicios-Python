moeda = float(input('digite o valor a ser convertido: R$ '))
cotacao = float(input('digite o cotacao do dolar atual: U$ '))

print(' o valor R$ {:.2f} convertido com o Dolar a U$ {:.2f} é de: U$ {:.2f}'.format(moeda, cotacao, moeda / cotacao))
