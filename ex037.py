num1 = int(input('digite um numero: '))
print('ESCOLHA UMA DAS BASES PARA CONVERSÃO')
print('[ 1 ] converter para binario\n'
      '[ 2 ] converter para octal\n'
      '[ 3 ] converter para hexadecimal\n')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('o valor de {} convertido em binario é {}'.format(num1,bin(num1)))
elif opcao == 2:
    print('o valor de {} convertido em octal é {}'.format(num1,oct(num1)))
elif opcao == 3:
    print('o valor de {} convertido em hexadecimal é de {}'.format(num1, hex(num1)))
else:
    print('\n\33[7:4mdigitou errado seu retardado\33[m')
