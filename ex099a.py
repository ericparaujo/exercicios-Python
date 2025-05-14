from random import randint

maior = []
num_linhas = randint(1, 6)

for l in range(num_linhas):
    linha = []
    cont = randint(1, 7)
    for c in range(cont):
        linha.append(randint(1, 10))
    maior.append(linha)

flat_maior = [item for sublist in maior for item in sublist]
maior_numero = max(flat_maior)


print("Matriz gerada:")
for linha in maior:
    print(linha)
print(f'Quantidade de números: {len(flat_maior)}')
print(f'O maior número é: {maior_numero}')