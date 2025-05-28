num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
num3 = int(input('digite mais um numero: '))
num4 = int(input('digite o ultimo numero: '))

tupla = (num1, num2, num3, num4)

print(f'voce digitou os valores: {tupla}')
print(f'voce digitou nove {tupla.count(9)} vezes')
print(f'o 3 apareceu na posicao: {tupla.index(3)}')

for n in tupla:
    if n % 2 ==0:
        print(n, end = ' ')