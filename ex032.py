ano = int(input('digite o ano a qual quer saber: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('esse ano é bisexto')
else:
    print('esse ano nao é bisexto')
