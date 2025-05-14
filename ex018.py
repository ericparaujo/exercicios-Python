import math
angu = float(input('digite o angulo que deseja saber: '))
sen = math.sin(math.radians(angu))
cos = math.cos(math.radians(angu))
tan = math.tan(math.radians(angu))
print('Com o angulo de {}°, \n '
      'O valor de seno é {:.2f}, \n '
      'O valor de cosseno é: {:.2f}\n '
      'O valor da tangente é {:.2f}'.format(angu, sen, cos, tan))
