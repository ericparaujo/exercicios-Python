def ficha(jogador, gol=0):
    if len(jogador) == 0:
        jogador = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0


    print(f'o jogador {jogador} fez {gol} gols')

    return jogador, gol


nome = str(input('digite o nome do jogador: ')).strip()
gols = str(input('numero de gols: '))

ficha(nome, gols)
