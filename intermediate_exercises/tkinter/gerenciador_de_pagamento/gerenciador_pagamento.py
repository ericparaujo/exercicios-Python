"""
COMO TUDO FUNCIONA JUNTO:

1. __init__.py cria a janela com os elementos visuais
2. Quando o usuário clica em "Calcular":
   a) Chama calcular_valor() do gerenciador_pagamento.py
   b) calcular_valor() chama entrada_dados() para validar
   c) entrada_dados() usa mensagens de erro do estilos.py
   d) Se tudo ok, faz o cálculo e retorna o resultado
   e) O resultado é mostrado na janela principal
"""

"""
GERENCIADOR_PAGAMENTO:

Cérebro do programa.
Faz os cálculos de pagamento e valida os dados digitados pelo usuário.
É onde a mágica matemática acontece!
"""

from tkinter import messagebox
import estilos


def entrada_dados(entrada_valor, entrada_opcao) -> (float, str):
    """
    Valida o que o usuário digitou.
    :parameter:
    - Pega o valor digitado e tenta converter para número
    - Verifica se é um valor válido (maior que zero)
    - Pega a opção de pagamento selecionada
    - Se encontrar erro, mostra mensagem adequada
    :return:
    Retorna valor convertido e opção ou (None, None) se tiver erro
    """

    valor_validar = entrada_valor.get().strip().replace(',', '.')
    valor = float
    opcao = str(entrada_opcao.get())
    mensagem = estilos.mensagem_erro()

    if not valor_validar:
        messagebox.showerror('ERRO', mensagem[0]) # Campo valor vazio

    try:
        valor = float(valor_validar)
        if valor <= 0:
            messagebox.showerror('ERRO', mensagem[1]) # Valor zerado/negativo
            return None, None

    except ValueError or TypeError:
        messagebox.showerror('ERRO', mensagem[2]) # Valor não numérico

    return valor, opcao


def calcular_valor(entrada_valor, entrada_opcao, opcoes_pagamento) -> str:
    """
    Calcula o valor final do produto.
    :parameter:
    * Usa o valor e a forma de pagamento para:
    - Aplicar 5% de desconto para pagamento à vista
    - Manter valor original para cartão à vista
    - Aplicar 5% de juros para parcelamento em 2x
    - Aplicar 8% de juros para parcelamento em mais vezes
    :return:
    Retorna o valor formatado como "Total a pagar: R$ XX.XX"
    """

    valor, opcao = entrada_dados(entrada_valor,entrada_opcao)
    forma_pagamento = opcoes_pagamento
    total =  float
    mensagem = estilos.mensagem_erro()


    if opcao not in opcoes_pagamento:
        messagebox.showerror('ERRO', mensagem[3]) # Pagamento não selecionado

    elif opcao == forma_pagamento[0]:
        total = valor - (valor * 0.05)
    elif opcao == forma_pagamento[1]:
        total = valor
    elif opcao == forma_pagamento[2]:
        total = valor + (valor * 0.05)
    elif opcao == forma_pagamento[3]:
        total = valor + (valor * 0.08)

    return f'Total a pagar: {total:.2f}'

