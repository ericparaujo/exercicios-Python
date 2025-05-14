times = (' Palmeiras ', ' Grêmio ', ' Atlético-MG ', ' Flamengo ', ' Botafogo ', ' Bragantino ', ' Fluminense ',
         ' Athletico-PR ', ' Internacional ', ' Fortaleza ', ' São Paulo ', ' Cuiabá ', ' Corinthians ',
         ' Cruzeiro ', ' Vasco ', ' Bahia ', ' Santos ', ' Goiás ', ' Coritiba ', ' América-MG ')


print(f'os 5 primeiros times sao: {times[:5]}')
print(f'os quatro ultimos sao: {times[-4:]}')
print(f'organizado em ordem alfabetica: {sorted(times)}')
print(f'o vasco esta na posicao: {times.index(" Vasco ") + 1}')
