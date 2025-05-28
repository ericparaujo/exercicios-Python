dic = {'nome': str(input('digite o nome: ')),
       'media': float(input('digite a media: '))}

if dic['media'] <= 4:
    dic['situacao'] = 'reprovado'
elif dic['media'] <= 6:
    dic['situacao'] = 'recuperacao'
else:
    dic['situacao'] = 'aprovado'

for k, v in dic.items():
    print(f'{k} é igual a {v}')
