'''def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    elif 29.9 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 34.9 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"


# Solicitação dos dados ao usuário
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Classificação do IMC
classificacao = classificar_imc(imc)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")'''


def formula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def tabela_imc(imc):
    def cores():
        return {
            'limpar': '\033[m',
            'preto': '\033[30m',
            'vermelho': '\033[31m',
            'verde': '\033[32m',
            'amarelo': '\033[33m',
            'azul': '\033[34m',
            'magenta': '\033[35m',
            'ciano': '\033[36m',
            'cinza': '\033[37m',
            'branco': '\033[97m'
        }

    if imc < 17:
        return 'esta muito abaixo do peso', cores()['vermelho']
    elif imc <= 18.49:
        return 'esta abaixo do peso', cores()['amarelo']
    elif imc <= 24.99:
        return 'esta com o peso normal', cores()['verde']
    elif imc <= 29.99:
        return 'esta acima do peso', cores()['azul']
    elif imc <= 34.99:
        return 'esta com OBESIDADE NIVEL I', cores()['magenta']
    elif imc <= 39.99:
        return 'esta com obesidade nivel II (severa)', cores()['ciano']
    else:
        return 'esta com OBESIDADE III (mórbida)', cores()['branco']


'''def cores():
    return {
        'limpar': '\033[m',
        'preto': '\033[30m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'magenta': '\033[35m',
        'ciano': '\033[36m',
        'cinza': '\033[37m',
        'branco': '\033[97m'
    }'''


# Entradas de dados para a fórmula
peso = float(input('qual é seu peso? '))
altura = float(input('qual a sua altura? '))

# Cálculos e resultados
formula = formula_imc(peso, altura)
tabela, cor = tabela_imc(formula_imc(peso, altura))

# Impressão do resultado com a cor apropriada
print(f'seu indice de massa corporal (IMC) é de {cor}{formula:.2f}, ', end='')
print(f'{cor}Você {tabela}')
