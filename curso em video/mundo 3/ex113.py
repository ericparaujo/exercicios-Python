def leiaInt(num):
    while True:
        try:
            n = int(input(num))

        except (ValueError, TypeError):
            print('digite um numero valido.')
            continue

        except (KeyboardInterrupt):
            return 0

        else:

            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input(num))

        except (ValueError, TypeError):
            print('digite um numero valido.')

        except (KeyboardInterrupt):
            print('operacao interrompida pelo usuario')
            return 0

        else:
            return n


inteiro = leiaInt('digite um numero: ')
real = leiaFloat('digite um numero: ')
print(f'inteiro: {inteiro}\n'
      f'real: {real}')
