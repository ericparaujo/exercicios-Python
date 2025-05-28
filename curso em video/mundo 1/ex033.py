num1 = int(input('digite um numero: '))
num2 = int(input('digite o 2° numero: '))
num3 = int(input('digite o 3° numero: '))

if num1 > num2 > num3:
    maior = num1
    menor = num3
if num2 > num1 > num3:
    maior = num2
    menor = num3
if num2 > num3 > num1:
    maior = num2
    menor = num1
if num3 > num2 > num1:
    maior = num3
    menor = num1
if num3 > num1 > num2:
    maior = num3
    memor = num3
if num1 > num3 > num2:
    maior = num1
    menor = num2

print('o maior é {}'.format(maior))
print('o menor é {}'.format(menor))
