"""
 Conversor de medidas
Objetivo: Converter um valor em metros para outras unidades de medida: centímetros, milímetros, quilômetros, etc.

Detalhes: O usuário digita um valor em metros, e o programa mostra a conversão para múltiplas unidades.
"""


def interface():
    """
    Exibe o menu de opções para o usuário escolher a unidade de destino da conversão.

    Mostra as opções disponíveis:
    1 - milímetro
    2 - centímetro
    3 - quilômetro
    """

    print('ESCOLHA A UNIDADE DE DESTINO \n'
          + f'====' * 7 + '\n'
          '(1) - milimetro \n'
          '(2) - centimetro \n'
          '(3) - quilometro \n')


def entradaDados() ->tuple[int, float]:
    """
    Solicita e captura os dados de entrada do usuário.

    Apresenta a interface de escolha e pede que o usuário selecione a unidade de destino
    e informe o valor em metros a ser convertido.

    :return: Uma tupla contendo a unidade de destino (int) e o valor em metros (float)
    """

    interface()
    unidade_destino = int(input('escolha a unidade de destino: '))
    valor_unidade = float(input('digite o valor a ser convertido em metros: '))
    return unidade_destino, valor_unidade


def conversor(unidade_destino, valor_unidade = float) ->float:
    """
     Converte o valor em metros para a unidade de destino escolhida.

    :param unidade_destino: Código da unidade para qual o valor será convertido (1-mm, 2-cm, 3-km)
    :param valor_unidade: Valor em metros a ser convertido
    :return: O valor convertido para a unidade de destino
    """

    formulas = (1000, 100, 0.001)
    valor_destino = valor_unidade * formulas[unidade_destino - 1]
    return valor_destino


def saidaDados() -> None:
    """
    Gerencia o fluxo principal do programa e exibe o resultado da conversão.

    Obtém os dados de entrada do usuário, realiza a conversão e apresenta
    o resultado formatado na tela.
    """

    unidade_destino, valor_unidade = entradaDados()
    valor_convertido = conversor(unidade_destino)
    unidades = ('mm', 'cm', 'km')

    print(f'o valor de {valor_unidade}m equivale a {valor_convertido}{unidades[unidade_destino - 1]}')



if __name__ == '__main__':
    saidaDados()