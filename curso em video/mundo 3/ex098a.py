from time import sleep

def contador(x, y, z):
    print('===' * 10,'\n')
    print(f'contador de {x} até {y} pulando {z} numeros: ')
    for c in range(x, y, z):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('\n')


num = [int(input('\n\ndigite o numero inicial: ')),
       int(input('digite o numero final: ')),
       int(input('digite o salto: '))]

contador(0, 11, 1)
contador(10, 0, -2)

contador(num[0], num[1], num[2])
