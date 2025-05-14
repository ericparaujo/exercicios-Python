km = int(input('digite quantos km é sua viagem '))
if km <= 200:
    print('No percurso de {}km, o valor da viagem é de R${:.2f} '.format(km, km * 0.5))
else:
    print('no percurso de {}km, o valor da viagem é de R${:.2f}'.format(km, km * 0.45))

