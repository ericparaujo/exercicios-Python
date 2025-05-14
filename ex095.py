jogadores = dict()
time = list()
gols = list()
continuar = 'S'

while True:
    if continuar in 'S':
        jogadores['nome'] = str(input('digite o nome do jogador: ')).upper().strip()
        jogadores['partidas'] = int(input('digite a quantidade de partidas jogadas: '))

        for c in range(0, jogadores['partidas']):
            gols.append(int(input(f'quantos gols fez na {c + 1}º partida: ')))
            jogadores['gols'] = gols.copy()

        time.append(jogadores.copy())
        gols.clear()
        jogadores.clear()

    elif continuar in 'N':
        break

    else:
        print('DIGITE NOVAMENTE, [S/N]')

    continuar = str(input('deseja continuar: [ S/N ] ')).upper().strip()

print()
print('===' * 20)
print(' COD   NOME                   GOLS                TOTAL')
print('---' * 20)

for k, v in enumerate(time):
    print(f'{k:<5}  {v['nome']:<15} {"":>5}  {v['gols']}   {sum(v['gols']):>10}')

print('===' * 20)

while True:
    estatistica = int(input('\nqual jogador deseja saber informacoes: [999 para sair]'))

    if estatistica <= len(time):
        if estatistica == 999:
            break

        else:
            print(f'levantamento do jogador {time[estatistica]['nome']}: ')
            for k, v in enumerate(time[estatistica]['gols']):
                print(f'no jogo {k + 1} fez {v}')
            print(f'total = {sum(time[estatistica]['gols'])}')

    else:
        print('codigo errado, tente novamente')
