total = []
par = []
impar = []

while True:
     num = int(input('digite um numero: '))
     continuar = str(input('deseja continuar: [S / N] ')).lower()
     total.append(num)

     if num % 2 == 0:
      par.append(num)
     else:
      impar.append(num)

     if continuar == 'n':
         break
     #if continuar == 's':


print(f'o total é: {total}')
print(f'o par é: {par}')
print(f'o impar é: {impar}')
