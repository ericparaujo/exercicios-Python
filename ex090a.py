def curso():
    c = 's'
    lista = []
    dic = {}
    while True:
        print('-------')

        if c == 's':


            dic['aluno'] = str(input('digite o nome do aluno: ').strip())
            dic['nota'] = float(input('digite a nota: '))

            if dic['nota'] <= 4.9:
                dic['resultado'] = 'reprovado'

            elif dic['nota'] <= 5.9:
                dic['resultado'] = 'recuperacao'

            elif dic['nota'] <= 10:
                dic['resultado'] = 'APROVADO'

            else:
                dic['resultado'] = 'valor invalido'
            # curso()
            c = str(input('deseja continuar[s/n]: ').strip())

        elif c == 'n':
            print('obrigado')
            break

    lista = dic

    return lista


#def tabela():





print(curso())

for k, v in curso().items():
    print(f'{k} : {v}')

