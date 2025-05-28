from time import sleep


def contador(inic, fin, salt):
    print('=' * 40)

    if salt == 0:
        print('impossivel contar com numero ZERO')
    if inic < fin:
        fin += 1
    else:
        fin -= 1
        if salt > 0:
            salt *= -1
    for c in range(inic, fin, salt):
        print(f'{c}', end=' ')
        sleep(0.5)
    print(' FIM')


contador(1, 10, 1)
contador(10, 1, -2)

inicio = int(input('digite o numero inicial: '))
final = int(input('digite o numero final: '))
salto = int(input('digite o valor dos saltos: '))

contador(inicio, final, salto)
