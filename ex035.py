lado1 = float(input('digite o valor do 1° lado do triangulo: '))
lado2 = float(input('digite o valor do 2° lado do triangulo: '))
lado3 = float(input('digite o valor do 3° lado do triangulo: '))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print('é um triangulo')
else:
    print('nao é um triangulo')