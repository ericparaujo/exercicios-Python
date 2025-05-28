contador = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('digite um numero de zero a vinte: '))
    if 0 <= num <= 20:
        print(contador[num])
        break
    else:
        print('digitou errado')