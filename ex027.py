nome = str(input('digite seu nome todo: ')).strip().upper()
separado = nome.split()
print('o primeiro nome é {}'.format((nome.split())[0]))
print('o ultimo nome é {}'.format(separado[len(separado)-1]))
