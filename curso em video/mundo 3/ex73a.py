classificacao = ('PALMEIRAS','BOTAFOGO','GRÊMIO','RED BULL BRAGANTINO','ATLÉTICO-MG','FLAMENGO','ATHLETICO-PR',
                 'FLUMINENSE','CUIABÁ','SÃO PAULO','CORINTHIANS','FORTALEZA', 'INTERNACIONAL','SANTOS','VASCO','BAHIA',
                 'CRUZEIRO','GOIÁS','CORITIBA','AMÉRICA-MG')

print(f'a ordem dos 5 primeiros sao: {classificacao[:5]}')
print(f'a ordem dos 5 ultimos sao: {classificacao[-4:]}')
print(f'os times em ordem alfabetica é: {sorted(classificacao)}')
print(f'o fluminense esta na posicao: {classificacao.index("FLUMINENSE")}')