'''calculo de triangulo retangulo'''
catOp = float(input('digite o valor do cateto oposto: '))
catAd = float(input('digite o valor do cateto adjacente: '))
hipo = ((catOp ** 2) + (catAd ** 2)) ** (1/2)
print('o valor da hipotenusa é: {}'.format(hipo))
'''outra forma'''
from math import sqrt
print('o valor da hipotenusa é: {}'.format(sqrt((catOp ** 2) + (catAd ** 2))))
