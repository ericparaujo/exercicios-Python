alt = float(input('digite a altura da parede em metros: '))
larg = float(input('digite a largura da parede em metros: '))
area = alt * larg
tinta = area / 2
print('a area de sua parede é de {:.2f}m², entao, sera nescessario {:.2f} litros de tinta para pintar a parede'.format(area, tinta))
