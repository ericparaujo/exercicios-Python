num = int(input('digite um numero: '))
contador = num + 1
total = 1
f = 1

while contador > 1:
    total = num * contador
    contador -= 1
    f *= contador

    print(contador)
print(f)