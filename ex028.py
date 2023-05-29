'''import random
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
res = int(input('Qual numero vc acha que a maquina escolheu entre 0 e 5? '))
if escolhido == res:
    print('Parabens vc acertou!')
else:
    print('Sinto muito o numero erra {}, mais sorte da proxima!!'.format(escolhido))'''

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou prnsar em um número estre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
print('processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! você conseguiu me vencer!')
else:
    print('Ganhei! eu pensei no número {} e não no {}!'.format(computador, jogador))