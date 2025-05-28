from ex115.lib.arquivo import *

arq = 'tabela.txt'

if arquivo_existe(arq):
    print('arquivo encontrado')
else:
    print('arquivo nao encontrado')
    criar_arquivo(arq)

while True:
    resposta = menu(['visualizar cadastro', 'novo cadastro', 'sair do sistema'])
    if resposta == 1:
        ler_arquivo(arq)

    elif resposta == 2:
       nome = str(input('nome: '))
       idade = opcao('idade: ')
       cadastrar(arq, nome, idade)

    elif resposta == 3:
        print('opcao 3')
        break
    else:
        print('opcao invalida')
