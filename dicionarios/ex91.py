from random import randint
from time import sleep
from operator import itemgetter

# cabecalho
print('=-' * 20)
print(f'{"Desafio 91":^40}')
print('-' * 40)
print()

jogadores = {}

for c in range(1, 5):
    key = 'jogador' + str(c)
    jogadores[key] = randint(1, 6)
    print(f'Jogador{c}: {jogadores[key]}')
    sleep(.5)

ranking = sorted(
    jogadores.items(), 
    key=itemgetter(1), 
    reverse=True
)
print()

print('-' * 40)
print(f'{"| RANKING |":^40}')
print('-' * 40)

for c, dado in enumerate(ranking):
    print(f'Em {c + 1}º lugar: {dado[0]} com {dado[1]}')

# rodape
print()
print('=-' * 20, '\n')