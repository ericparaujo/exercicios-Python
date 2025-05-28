total = 0
cont = 0
num = int(input('digite um numero ( Digite [999] para sair) : '))

while num != 999:
    total += num
    cont += 1
    num = int(input('digite um numero ( Digite [999] para sair) : '))

print(total)
