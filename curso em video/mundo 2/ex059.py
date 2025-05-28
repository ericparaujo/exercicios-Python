num1 = float(input('digite um numero: '))
num2 = float(input('digite outro numero: '))
escolha = False
opcao = 0

while opcao != 5:
    print('digite uma opcao: ')
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos numeros\n'
          '[5] sair do programa\n')
    opcao = int(input('opcao: '))

    if opcao == 1:
        soma = num1 + num2
        print(f'a soma de {num1} + {num2} = {soma}')
    elif opcao == 2:
        multiplicacao = num1 * num2
        print(f'a multiplicacao de {num1} x {num2} = {multiplicacao}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'o maior numero é{maior}')
    elif opcao == 4:
        print('iniciando novo calculo:')
        num1 = float(input('digite um numero: '))
        num2 = float(input('digite outro numero: '))
    elif opcao == 5:
        print('até mais ...')
    else:
        print('opcao invalida, tente novamente')
