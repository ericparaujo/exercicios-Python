lado1 = float(input('digite o valor de um dos lados do triangulo: '))
lado2 = float(input('digite o valor de outro lado do trangulo: '))
lado3 = float(input('digite o valor do terceiro lado do triangulo: '))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print('é um triangulo')
    if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('do tipo ISÓSCELES')
    elif lado1 == lado2 == lado3:
        print('do tipo EQUILÁTERO')
    else:
        print(' do tipo ESCALENO')
else:
    print('nao é triangulo')