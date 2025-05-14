salario = float(input('digite o valor do salario: '))
if salario <= 1250:
    por100 = 0.15
else:
    por100 = 0.10

print('o valor de R${:.2f} teve {:.0f}% de aumento indo para R${:.2f}'
      .format(salario, (por100 * 100), (salario * por100) + salario))
