"""
Gerenciador de pagamentos
Leia o preço de um produto e ofereça opções de pagamento (à vista, parcelado, etc.),
aplicando descontos ou juros conforme escolha.
"""


def entrada_dados(entrada_valor, entrada_opcao):
    try:

        valor_validar = entrada_valor.get().strip().replace(',', '.')
        valor = float(valor_validar) if valor_validar else None
        opcao = str(entrada_opcao.get())

        if valor <= 0 or valor is None:
            return None, 'Valor invalido'

        return valor, opcao

    except ValueError and TypeError:
        print('entrada invalida')



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

    except ValueError:
        print('opcao invalida!')




#print(f'valor total: {calcular_valor()}')
