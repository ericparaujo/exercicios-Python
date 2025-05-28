celsius = float(input('digite a temperatura em graus celsius a qual deseja converter °c: '))
convert = (celsius * (9 / 5) + 32)
print('a temperatura digitada foi de {:.1f}°c que equivale a {:.1f}°f'.format(celsius, convert))
