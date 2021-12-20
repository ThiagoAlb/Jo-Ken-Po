import random
from time import sleep

jogador = int(input('''OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA 
Qual a sua opção? '''))

print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PO!!!')
sleep(0.6)

print('-='*20)
if jogador == 0:
    print('Você escolheu: PEDRA')
elif jogador == 1:
    print('Você escolheu: PAPEL')
elif jogador == 2:
    print('Você escolheu: TESOURA')
else:
    print('Escolha um número de 0 até 2')

palavras = ['PEDRA', 'PAPEL', 'TESOURA']
def selectRandom(palavras):
    return random.choice(palavras)

computador = selectRandom(palavras)
print('O computador escolheu:', computador)
print('-='*20)

if computador == 'PEDRA':
    if jogador == 0:
        print('\33[1;45mEMPATE\33[m')
    elif jogador == 1:
        print('\33[1;41mCOMPUTADOR VENCE\33[m')
    elif jogador == 2:
        print('\33[1;42mJOGADOR VENCE\33[m')
    else:
        print('\33[1;31mJogada inválida!\33[m')
elif computador == 'PAPEL':
    if jogador == 0:
        print('\33[1;41mCOMPUTADOR VENCE!\33[m')
    elif jogador == 1:
        print('\33[1;45mEMPATE!\33[m')
    elif jogador == 2:
        print('\33[1;42mJOGADOR VENCE!\33[m')
    else:
        print('\33[1;31mJogada inválida!\33[m')
elif computador == 'TESOURA':
    if jogador == 0:
        print('\33[1;42mJOGADOR VENCE!\33[m')
    elif jogador == 1:
        print('\33[1;41mCOMPUTADOR VENCE!\33[m')
    elif jogador == 2:
        print('\33[1;45mEMPATE!\33[m')
    else:
        print('\33[1;31mJogada inválida!\33[m')