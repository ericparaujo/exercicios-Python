import moeda

valor = float(input('digite um valor: R$ '))
porcento_mais = int(input('digite a porcentagem a ser adcionada: '))
porcento_menos = int(input('digite a porcentagem a ser subtraida: '))

moeda.resumo(valor, porcento_mais, porcento_menos)
