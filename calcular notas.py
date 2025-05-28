def calcular_notas(nota1: float, nota2: float)->float:
    """
        Calcula a média aritmética simples entre duas notas.

        Parâmetros:
        :param nota1: float - Valor da primeira nota (de 0 a 10)
        :param nota2: float - Valor da segunda nota (de 0 a 10)

        :return: float - Média das duas notas calculada por (nota1 + nota2) / 2
        """
    return (nota1 + nota2)/2


def entrada_notas()->float:
    """
    Coleta duas notas digitadas pelo usuário e retorna sua média.

    Fluxo:
    1. Solicita a primeira nota via input
    2. Solicita a segunda nota via input
    3. Converte ambas para float
    4. Retorna o resultado de calcular_notas com as notas inseridas

    :return: float - Média calculada das duas notas informadas
    """

    nota1 = float(input('entre com a nota: '))
    nota2 = float(input('entre com outra nota: '))
    return calcular_notas(nota1, nota2)


def numero_de_entradas()->int:
    """
       Solicita e retorna a quantidade de médias que serão calculadas.

       O usuário informa via input quantos conjuntos de notas
       serão processados posteriormente.

       :return: int - Número total de médias que serão calculadas
       """

    numero_entradas = int(input('quantas notas serao calculadas: '))
    return numero_entradas


print(entrada_notas())