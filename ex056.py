somaidade = 0
maior_idade = 0
nome_velho = ''
contador = 0

for pessoas in range(1,5):
    print('---' * 10, f'digite as informacoes da {pessoas}° pessoa', '---' * 10)
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()

    somaidade += idade
    if sexo == 'm':
       if maior_idade < idade:
         maior_idade = idade
         nome_velho = nome

    if sexo == 'f':
        if idade < 20:
            contador += 1


mediaidade = somaidade / 4
print(f'a maior idade é {maior_idade}\n'
      f'a media das idades é {mediaidade}\n'
      f'a pessoa mais velha é {nome_velho} ')
print(f'foram encontrados {contador} mulheres abaixo dos 20 anos')