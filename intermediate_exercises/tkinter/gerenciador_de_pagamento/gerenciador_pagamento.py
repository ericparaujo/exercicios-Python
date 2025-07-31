"""
Gerenciador de pagamentos
Leia o preço de um produto e ofereça opções de pagamento (à vista, parcelado, etc.),
aplicando descontos ou juros conforme escolha.
"""
from tkinter import messagebox
import estilos


def entrada_dados(entrada_valor, entrada_opcao):
    valor_validar = entrada_valor.get().strip().replace(',', '.')
    valor = float
    opcao = str(entrada_opcao.get())
    mensagem = estilos.mensagem_erro()

    if not valor_validar:
        messagebox.showerror('ERRO', mensagem[0])

    try:
        valor = float(valor_validar)
        if valor <= 0:
            messagebox.showerror('ERRO', mensagem[1])
            return None, None

    except ValueError or TypeError:
        messagebox.showerror('ERRO', mensagem[2])

    return valor, opcao


def calcular_valor(entrada_valor, entrada_opcao, opcoes_pagamento):
    valor, opcao = entrada_dados(entrada_valor,entrada_opcao)
    forma_pagamento = opcoes_pagamento
    total =  float
    mensagem = estilos.mensagem_erro()


    if opcao not in opcoes_pagamento:
        messagebox.showerror('ERRO', mensagem[3])

    elif opcao == forma_pagamento[0]:
        total = valor - (valor * 0.05)
    elif opcao == forma_pagamento[1]:
        total = valor
    elif opcao == forma_pagamento[2]:
        total = valor + (valor * 0.05)
    elif opcao == forma_pagamento[3]:
        total = valor + (valor * 0.08)

    return f'Total a pagar: {total:.2f}'

