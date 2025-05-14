nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = (nota1 + nota2) / 2
print('sua media foi {:.1f}'.format(media))

if media < 5:
    print('voce foi REPROVADO')
elif 5 <= media <= 6.9:
    print('voce esta em recuperacao')
else:
    print('voce foi APROVADO')
