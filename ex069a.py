cont_idade = cont_man = cont_girl = 0
while True:
    idade = int(input('digite a idade: '))
    sexo = sair = ' '

    while sexo not in 'FM':
        sexo = str(input('digite o sexo: [F/M]')).strip().upper()

    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_man += 1
    if sexo == 'F' and idade < 20:
        cont_girl += 1

    while sair not in 'SN':
        sair = str(input('deseja continuar: [S/N]')).strip().upper()

    if sair == 'N':
        break

print(f'sao {cont_idade} pessoas com mais de 18 anos')
print(f'sao {cont_man} homens no total')
print(f'sao {cont_girl} mulheres com menos de 20 anos')
print('FIM')
