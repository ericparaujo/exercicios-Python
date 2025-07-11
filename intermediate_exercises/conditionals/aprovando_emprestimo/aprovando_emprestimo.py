"""
 Aprovando empréstimo
Escreva um programa que leia o valor de uma casa, o salário do comprador e em quantos anos ele pretende pagar. Calcule o valor da prestação mensal e informe se o empréstimo será aprovado (prestação ≤ 30% do salário).
"""

from interface import bem_vindo, cores

def entrada_dados():
    valor_casa = float(input('Digite o valor da casa: R$ '))
    salario_comprador = float(input('Digite o salario do comprador: R$ '))
    parcelas = int(input('Digite quantos anos pretende pagar: '))
    return valor_casa, salario_comprador, parcelas


def calculo_prestacoes():
    valor_casa, salario_comprador, parcelas = entrada_dados()
    prestacoes = valor_casa / (parcelas * 12)
    saida = {'prestacoes':0,'salario':0}
    saida.update({'prestacoes': prestacoes, 'salario': salario_comprador})
    return saida


def condicoes_financiamento():
    financiamento = calculo_prestacoes()
    if financiamento['prestacoes'] <= financiamento['salario'] * 0.3:
        return f'\n{cores('azul').center(20)}Financiamento aprovado{cores('limpar')}'
    else:
        return f'\n{cores('amarelo')}Salario nao comporta o valor da casa!{cores('limpar')}'


def main():
    def deseja_continuar():


      while True:

            bem_vindo()
            print(condicoes_financiamento())
            continuar = str(input('deseja continuar [S/N]: ')).strip().upper()

            if continuar not in ['S', 'N']:
                print('Opção invalida! tente novamente')


            if continuar == 'N':
                print('Fim da operacao')
                break


    deseja_continuar()



    #bem_vindo()
    #print(condicoes_financiamento())


if __name__ == '__main__':
    main()