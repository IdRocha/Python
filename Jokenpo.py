from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas Opções:\
      [0] Pedra \
      [1] Papel \
      [2] Tesoura ')
jogador_s = input('Qual é a sua jogada? ')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
try:
    jogador = int(jogador_s)

    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('Jogador venceu!')
        elif jogador == 2:
            print('Computador venceu!') 
        else:
            print('Jogada inválida!')
    elif computador == 1:
        if jogador == 0:
            print('Computador venceu!')
        elif jogador ==1: 
            print("EMPATE!")
        elif jogador ==2:
            print('Jogador venceu!')
        else:
            print('Jogada inválida')
    elif computador ==2:
        if jogador == 0:
            print('Computador venceu!')
        elif jogador ==1:
            print('Jogador venceu!')
        elif jogador ==2:
            print('EMPATE!')
        else:
            print('Jogada inválida')
    else:
        print('Essa opção não existe.')
    print('-='*14)
    print('O computador escolheu {}'.format(itens[computador]))
    print('O jogador escolheu {}'.format(itens[jogador]))
    print('-='*14)    
except:
    print('Você não digitou uma opção válida!')