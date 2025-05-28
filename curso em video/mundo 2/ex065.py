soma = maior = menor = num = contador = 0
opcao = 's'

while opcao in 'Ss':
    num = int(input('digite um numero: '))
    soma += num
    contador += 1
    if menor == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    opcao = str(input('deseja continuar [S/N} : '))
    continuar = opcao

media = soma / contador
print(f'o maior é {maior}')
print(f'o menor é {menor}')
print (f'a media foi {media}')
print(f'o total é {soma}')
print(f'foram usados {contador} numeros no calculo')