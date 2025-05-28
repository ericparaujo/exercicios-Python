def area(largura, comprimento):

    area = largura * comprimento
    return area


l = float(input('digite a largura: '))
c = float(input('digite o comprimento: '))
print(f'a area total é de: {area(l, c)}M²')