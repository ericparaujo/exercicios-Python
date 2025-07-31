"""
Arquivo de estilos e mensagens.
Define como os textos aparecem na janela e as mensagens de erro usadas no programa.

"""

def estilos_fontes() -> dict:
    """
    Define os estilos de letra usados no programa.
    :return:
    * Retorna um dicionário com vários tamanhos e estilos de fonte:
    - 'titulo': Fonte grande e negrita para títulos
    - 'texto1': Fonte média negrita para campos importantes
    - 'texto2': Fonte média normal para textos comuns
    - 'botao': Fonte grande e negrita para o botão
    - 'resultado': Fonte grande e negrita para mostrar resultados
    """

    return {
        'titulo':('arial', 18, 'bold'),
        'texto1':('arial', 14, 'bold'),
        'texto2':('arial', 14),
        'botao':('arial', 16, 'bold'),
        'resultado':('arial', 20, 'bold')
    }


def exibir_textos():
    """
Fornece todos os textos usados na janela principal.
:return:
* Retorna um dicionário com:
- Título do programa
- Rótulo do campo de valor
- Rótulo do menu de pagamento
- Texto do botão calcular
"""
    return{
        'titulo':'Gerenciador de pagamento'.center(50).upper(),
        'valor_produto':'Valor do produto:',
        'forma_pagamento':'Forma de pagamento:',
        'botao':'Calcular'
    }


def forma_pagamento():
    """
    Lista as opções de pagamento disponíveis.
    :return:
    - Retorna uma lista com 4 formas de pagamento:
    1. À vista no dinheiro
    2. À vista no cartão
    3. Parcelado em 2x
    4. Parcelado em mais vezes
    """

    return ['pagamento a vista no dinheiro',
            'pagamento a vista no cartao',
            'pagamento parcelado no cartao [2x]',
            'pagamento parcelado no cartao [+ vezes]']

def mensagem_erro():
    """
    Fornece mensagens de erro padronizadas.
    :return:
    * Retorna uma lista com mensagens para:
    - Campo valor vazio
    - Valor zerado/negativo
    - Valor não numérico
    - Pagamento não selecionado
    """
    return ['Digite o valor do produto',
            'O valor precisa ser maior que zero',
            'Digite apenas numeros inteiros ou decimais',
            'Selecione a forma de pagamento']
