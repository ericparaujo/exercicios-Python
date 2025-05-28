sexo = str(input('digite o sexo [M/F]: ')).strip().upper()

while sexo not in 'MF':
        print('voce digitou errado, tente novamente digitando o M para mascolino ou F para feminino')
        sexo = str(input('digite o sexo [M/F]: ')).strip().upper()

if sexo == 'M':
    print('\n\no sexo digitado é masculino')
else:
    print('\n\no sexo digitado é feminino')