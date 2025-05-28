frase = str(input('digite uma frase: ')).strip().upper()
junto = ('').join(frase.split())
inverso = ''
print(junto)

for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]

if junto == inverso:
    print(f'voce digitou {junto} e o inverso é {inverso}\n portanto é um palíndromo')
else:
    print(f'voce digitou {junto} e o inverso é {inverso}\n portanto nao é palíndromo')