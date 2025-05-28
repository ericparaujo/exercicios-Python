contador = 0
soma = 0
while True:
    num = int(input('digite um numero: ( Digite [999] para sair): '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'foram digitados {contador} numeros e a soma é {soma}')