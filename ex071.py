print('==='* 7)
print('BANCO AGIOTA')
print('===' * 7)
saque = int(input(' QUAL VALOR DESEJA SACAR: R$'))
total = saque
cedula = 50
contador = 0

while True:
    #continuar = 'S'
    #while continuar in 'S':

    if total >= cedula:
        total -= cedula
        contador += 1
        print(contador)
    else:
        print(f'foram um total de {total} notas de {cedula} ')

        if cedula == 50:
            cedula = 20
        if cedula == 20:
            cedula = 10
        if cedula == 10:
            cedula = 1

        if total == 0:
            break

        print(contador)

    #continuar = str(input('deseja continuar [S/N]? ')).strip().upper()

    #if continuar not in 'SN':
    #    print('\nCOMANDO INVALIDO.\n\nTENTE NOVAMENTE')
    #if continuar == 'N':
    #    print('\nOBRIGADO\n\nVOLTE SEMPRE')
    #    break