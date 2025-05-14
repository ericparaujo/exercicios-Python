print('==' * 7)
print('\033[1;31mGerador de PA\033[m')
print('==' * 7)

termo = int(input('digite o primeiro termo da PA: '))
razao = int(input('digite a razao: '))
progressao = termo
c = 10

while c > 0:
    print(progressao, ' --> ',end=(''))
    progressao += razao
    c -=1
print('FIM')
