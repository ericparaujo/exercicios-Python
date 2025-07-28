"""
Gerenciador de pagamentos
Leia o preço de um produto e ofereça opções de pagamento (à vista, parcelado, etc.),
aplicando descontos ou juros conforme escolha.
"""
from tkinter import messagebox

def entrada_dados(entrada_valor, entrada_opcao):
    valor_validar = entrada_valor.get().strip().replace(',', '.')
    valor = float
    opcao = str(entrada_opcao.get())

    if not valor_validar:
        messagebox.showerror('ERRO', 'Digite o valor do produto')

    try:

        valor = float(valor_validar)
    except ValueError:
        messagebox.showerror('ERRO', 'Digite apenas numeros inteiros ou decimais')

    if valor <= 0:
        messagebox.showerror('ERRO', 'O valor precisa ser maior que zero')
        return None, None


    return valor, opcao


def calcular_valor(entrada_valor, entrada_opcao, opcoes_pagamento):
    valor, opcao = entrada_dados(entrada_valor,entrada_opcao)
    forma_pagamento = opcoes_pagamento
    total =  float


    if opcao not in opcoes_pagamento:
        messagebox.showerror('ERRO', 'Selecione a forma de pagamento')

    if opcao == forma_pagamento[0]:
        total = valor - (valor * 0.05)
    if opcao == forma_pagamento[1]:
        total = valor
    if opcao == forma_pagamento[2]:
        total = valor + (valor * 0.05)
    if opcao == forma_pagamento[3]:
        total = valor + (valor * 0.08)

    return f'Total a pagar: {total:.2f}'


