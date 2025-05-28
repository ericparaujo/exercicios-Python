
def numeros():

    num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze',
           'treze', 'quatorze', 'quinze', 'dezesses', 'dezesete', 'dezoito', 'dezenove', 'vinte')

    try:
        num2 = int(input('digite o valor: '))
        if 0 <= num2 <=20:
            print('ok')
        else:
            print('valor invalido')
    finally:
        print('ok')



    num3 = num[num2]
    print(f'o valor digitado foi: {num3}')
    return num2

#num0 = int
numeros()
'''while True:
    if 0 <= numeros(num0) <= 20:
        print('obrigado')
        break

    else:
        print('numero incorreto')'''


