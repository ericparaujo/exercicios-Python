"""
Gerenciador de pagamentos
Leia o preço de um produto e ofereça opções de pagamento (à vista, parcelado, etc.), aplicando descontos ou juros conforme escolha.
"""

def entrada_dados():
    while True:
        try:
            valor = float(input('insira o valor de um produto: '))
            print('escolha uma opcao:\n'
                  '(1) - pagamento a vista no dinheiro\n'
                  '(2) - pagamento a vista no cartao\n'
                  '(3) - pagamento parcelado no cartao ( 2X )\n'
                  '(4) - pagamento parcelado no cartao ( + vezes )')
            opcao = int(input('opcao: '))
            if valor or opcao in float or int:
                return valor, opcao
            if opcao not in [1, 2, 3, 4]:
                continue


        except ValueError:
            continue


def calcular_valor():
    valor, opcao = entrada_dados()

    try:
        match opcao:
            case 1:
                total = valor - (valor * 0.05)
                return total
            case 2:
                total = valor
                return total
            case 3:
                total = valor + (valor * 0.05)
                return total
            case 4:
                total = valor + (valor * 0.08)
                return total
            case _:
                print('opcao invalida')

    except ValueError:
        print('opcao invalida!')




print(f'valor total: {calcular_valor()}')
