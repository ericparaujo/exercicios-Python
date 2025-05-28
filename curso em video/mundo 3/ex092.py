from datetime import datetime

nome = str(input('digite o nome: ')).upper().strip()
nascimento = int(input('digite o ano de nascimento: '))
carteira = int(input('digite o n° da carteira de trabalho ( 0 se nao tiver) : '))

data_atual = datetime.now()
idade = data_atual.year - nascimento

cadastro = {'nome': nome,
            'idade': idade,
            'ctps': carteira}

if carteira == 0:
    print()

else:
    cadastro['contratacao'] = int(input('digite o ano de contratacao: '))
    cadastro['salario'] = float(input('digite o valor do salario: '))
    cadastro['aposentadoria'] = (cadastro['contratacao'] + 64) - data_atual.year

print('\n\n============================\n')

for k, v in cadastro.items():
    print(f'- {k} tem o valor de {v}')
