''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


# qual o valor da casa?
# qual o salario do comprador?
# qual tempo de prestacao?

# tempo = anos x 12
#prestacao = valor_da_casa / tempo

# se prestacao <= salario * 0,7:
#imprimir ('credito aprovado')
#senao:
#imprimir ('emprestimo negado')

print('\n\n')
print('\033[31m==''\033[32m==' '\033[33m=='*15, '\033[m\n')
print('\33[1:34mbem vindo ao sistema de credito, onde vc faz emprestimos e paga dando o rabo\33[m\n')
print('\033[31m==''\033[32m==' '\033[33m=='*15, '\033[m\n')
valor_casa = float(input('digite o valor do imovel a ser financiado: R$'))
salario = float(input('digite o seu salario: R$'))
anos = float(input('digite o tempo (em anos) total de seu fianciamento: '))

tempo = anos *12
prestacao = valor_casa / tempo

if prestacao <= salario * 0.3:
    print('\n\33[32mno total sao {:.0f} prestacoes no periodo de {:.0f} anos. o valor das prestacoes ficou em R${:.2f}'.format(tempo, anos, prestacao))
    print('\n\33[35mEmprestimo aprovado\33[m')
    print('\n\33[4magora de o cu pra pagar\33[m')
else:
    print('\n\33[36mseu emprestimo foi negado')
    print('\n\33[37mse fudeu seu babaca')