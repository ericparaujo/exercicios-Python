dias = int(input('por quantos dias o carro foi alugado: '))
km = float(input('quantos km foram rodados nesse periodo: '))
valorDias = dias * 60
valorKM = km * 0.15
print('o total a pagar é: R${:.2f}'.format(valorDias + valorKM))
