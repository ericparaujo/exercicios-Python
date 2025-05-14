num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))

if num1 > num2:
    print('o numero {} é maior que {}'.format(num1, num2))

elif num1 < num2:
    print('o numero {} é maior que {}'.format(num2, num1))

else:
    print('o numero {} e o numero {} sao os iguais'.format(num1, num2))

