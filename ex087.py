matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
coluna3 = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite o valor da natriz [{l}, {c}]: '))

print('=====' * 5)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')

        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 0:
            maior = matriz[1][c]
        elif matriz[1][c] >= maior:
            maior = matriz[1][c]
    if matriz[l][2] != 0:
        coluna3 += matriz[l][2]

    print()


print('=====' * 5)

print(f'a soma dos numeros pares é: {par}')
print(f'a soma da coluna 3 é: {coluna3}')
print(f'o maior numero da segunda coluna é: {maior}')


