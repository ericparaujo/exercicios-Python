num = float(input('digite um valor: '))
numint = int(num)
print('o valor digitado foi {} e seu valor arredondado é {} '.format(num, numint))

# metodo 2
#import math
from math import trunc
# num2 = float(input('digite outro numero: '))
#print('o valor digitado foi: {} e o valor arredondado é {}'.format(num, math.trunc(num)))
print('o valor arrendondado é {}'.format(trunc(num))
