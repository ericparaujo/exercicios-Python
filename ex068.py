from random import randint

contador = 0

while True:
    num = int(input('digite um numero '))
    escolha = input('escolha par ou impar [P / I]: ').strip().upper()
    aleatorio = randint(0, 9)
    total = (num + aleatorio)
    while escolha not in 'PI':
        print('retardado')
        escolha = input('escolha par ou impar [P / I]: ').strip().upper()

    if total % 2 == 0:
        print('=-=-' * 7)
        print(f'voce jogou {num} \ne eu joguei {aleatorio}. \no total foi {total}\n \ndeu par')
        if escolha == 'P':
            print('e voce escolheu par')
            print('voce venceu')
            print('=-=-' * 7)
            contador += 1
        elif escolha == 'I':
            print('e voce escolheu impar')
            print('voce perdeu')
            break
        else:
            print('voce digitou a opcao errada. tente novamente')
    if total % 2 != 0:
        print(f'voce jogou {num} e eu joguei {aleatorio}. o total foi {total}\n\ndeu impar')
        if escolha == 'P':
            print('voce perdeu')
            break
        elif escolha == 'I':
            print('voce venceu')
            contador += 1
        else:
            print('voce digitou a opcao errada. tente novamente')

            
print('===' * 6)
print('GAME OVER')
print(f'voce teve {contador} vitorias')