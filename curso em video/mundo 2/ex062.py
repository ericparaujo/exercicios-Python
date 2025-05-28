termo = int(input('digite o primeiro termo da PA: '))
razao = int(input('digite a razao: '))
progressao = termo
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} --> ',end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos deseja mostrar a mais: '))
print(f'finalizado com {total} termos')

