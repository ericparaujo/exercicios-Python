"""
Custo da viagem: faça um programa que leia a distância de uma viagem em km. Calcule o preço da passagem cobrando R$ 0,50 por km para viagens até 200 km e R$ 0,45 por km para viagens mais longas
"""

from exercicios2.custoDeViagem.interface import bem_vindo, cores

bem_vindo()

def entrada_distancia() -> float:
    distancia_viagem = float(input('\nDigite a distancia da viagem (em KM): '))
    return distancia_viagem


def calcular_valores() -> float:
    distancia = entrada_distancia()
    if distancia <= 200:
        viagem = 0.5 * distancia
    else:
        viagem = 0.45 * distancia

    return viagem


def valor_viagem() -> None:
    print(f'\nO valor da viagem ficou em: R$ {cores.azul(4)}{calcular_valores():.2f} {cores.apagar()} ')


def deseja_continuar() -> None:
    while True:
        valor_viagem()
        continuar = str(input('\ndeseja realizar outra consulta de preço [S/N]: ')).strip().upper()

        if continuar not in ('S', 'N'):
            print(f'\n{cores.magenta()}opcao invalida, tente novamente!{cores.apagar()}')

        if continuar == 'N':
            print(f'\n{cores.verde()}Volte sempre!{cores.apagar()}')
            break


if __name__ == "__main__":
    deseja_continuar()
