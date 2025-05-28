while True:
    #conti = str(input('deseja continuar: [ S / N ]')).strip().upper()
    sexo = ''
    mulher = 0
    idade = 0
    homem = 0
    cont_idade = 0
    sair = 0
#    while sexo in 'FM':
    while sexo not in 'FM':
        sexo = str(input('digite o sexo: [ F / M ]')).strip().upper()

#       if sexo not in 'FM':
#           sair = 1
#           break

    idade = int(input('digite a idade: '))
    if sexo == 'F' and idade < 20:
        # if idade < 20:
        mulher += 1
        if idade > 18:
            cont_idade += 1
    elif sexo == 'M':
        homem += 1
        if idade > 18:
            cont_idade += 1



    print(f'homens: {homem}\n+18: {cont_idade}\nmulheres: {mulher}')
    #break


