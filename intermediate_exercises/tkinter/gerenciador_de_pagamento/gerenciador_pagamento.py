"""
Gerenciador de pagamentos
Leia o preço de um produto e ofereça opções de pagamento (à vista, parcelado, etc.),
aplicando descontos ou juros conforme escolha.
"""


def entrada_dados(entrada_valor, entrada_opcao):
    valor = float(entrada_valor.get())
    opcao = str(entrada_opcao.get())


    '''while True:
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
            continue'''

    return valor, opcao


def calcular_valor(entrada_valor, entrada_opcao, opcoes_pagamento):
    valor, opcao = entrada_dados(entrada_valor,entrada_opcao)
    forma_pagamento = opcoes_pagamento

    try:
        if opcao == forma_pagamento[0]:
            total = valor - (valor * 0.05)
        if opcao == forma_pagamento[1]:
            total = valor
        if opcao == forma_pagamento[2]:
            total = valor + (valor * 0.05)
        if opcao == forma_pagamento[3]:
            total = valor + (valor * 0.08)
        return f'Total a pagar: {total:.2f}'
            #case _:
                #print(opcao)

    except ValueError:
        print('opcao invalida!')




#print(f'valor total: {calcular_valor()}')
