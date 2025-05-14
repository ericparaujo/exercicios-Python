jogador = {'nome': str(input('nome do jogador: ')).upper().strip()}
partida = int(input(f'quantas partidas o {jogador["nome"]} jogou: '))
gols = []

for p in range(1, partida + 1):
    gols.append(int(input(f'    quantos gols na partida {p}: ')))

jogador['Gols'] = gols.copy()
jogador['total'] = sum(gols)

print('\n', '=========' * 5)
print(jogador)
print('========' * 5)

for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')

print('=' * 40)
print(f'o jogador {jogador["nome"]} realizou {len(jogador["Gols"])} partidas')

for p, v in enumerate(jogador['Gols']):
    print(f'    ==> na partida {p + 1} foram realizados {v} gols')

print(f'=' * 40)
print(f'foram realizados {jogador["total"]} gols')
