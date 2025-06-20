"""
Analisador de textos: faça um programa que leia uma frase qualquer e diga quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e a última

"""

def entrada_frase() -> tuple[str, str]:
    """
    Entrada de dados para as variaves frase e letra
    :return:variaves frase e letra
    """
    frase = str(input('digite uma frase: ')).strip().upper()
    letra = str(input('qual a letra deseja contar: ')).strip().upper()
    return frase, letra


def main() -> None:
    """
        Executa o processo principal do programa:
    - chama a função de entrada para obter a frase e a letra,
    - conta quantas vezes a letra aparece na frase,
    - imprime o resultado na tela.
    :return: sem retorno
    """
    frase, letra = entrada_frase()
    contador = frase.count(letra)
    print(contador)


if __name__ == "__main__":
    main()
