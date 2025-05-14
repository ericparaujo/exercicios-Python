while True:
    num = int(input('digite a tabuada a qual deseja aprender: '))
    if num < 0:
        print('tabuada encerrada')
        break

    for c in range(1,11,1):
        print(f'{num} X {c} = {num * c}')

print('volte sempre')