from random import choice
from time import sleep

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
npc = choice(opcoes)

print('\33[31m▓▓▓▓▓▓\33[m'*10)
print('\33[31m▓', '\33[1:32mBEM VINDO AO JOGO PEDRA, PAPEL E TESOURA\33[m'.center(66), '\33[31m▓')
print('\33[31m▓▓▓▓▓▓\33[m'*10)
print('\nESCOLHA UMA OPÇÃO: \n')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA\n')
escolha = int(input('qual sua escolha? \n'))

#FUNÇÃO DE PAUSA
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

#CONVERSAO DE NUMERO PARA OPCOES
voce = 'errado'
if escolha == 1:
    voce = 'PEDRA'
elif escolha == 2:
    voce = 'PAPEL'
elif escolha == 3:
    voce = 'TESOURA'
#elif voce == 'errado':
#    print('digitou opcao errada')
else:
    print('digitou opcao errada')

print('voce escolheu: \33[34m{}\33[m'.format(voce))
print('eu escolhi: \33[34m{}\33[m'.format(npc))


if voce == npc:
    print('\n \33[1:43mnós 2 EMPATAMOS\33[m')

elif (voce == 'PEDRA' and npc == 'PAPEL') or \
        (voce == 'PAPEL' and npc == 'TESOURA') or \
        (voce == 'TESOURA' and npc == 'PEDRA'):
    print('\n \33[1:43mVOCE PERDEU\33[m')

elif voce != 'PEDRA' or 'PAPEL' or 'TESOURA':
    print('TENTE NOVAMENTE')

else:
    print('\n \33[1:43mVOCE GANHOU\33[m')