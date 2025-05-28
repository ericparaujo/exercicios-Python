soma = 0
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        cont += +1
        soma += impar
print('a soma dos {} numeros impares multiplos de 3 é de {}'.format(cont, soma))

