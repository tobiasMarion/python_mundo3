from random import randint
from time import sleep

# cabecalho
print('=-' * 20)
print(f'{"Desafio 88":^40}')
print('-' * 40)
print()

print('-' * 40)
print(f'{"Números da Mega Sena":^40}')
print('-' * 40)
print()

numJogos = int(input('Digite o número de jogos para serem gerados: '))

for c in range(1, (numJogos + 1)):
    lista = []

    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        
        if len(lista) == 6: 
            break
    
    lista.sort()
    print(f'Os números do {c}º jogo são: {lista}')
    lista.clear()
    sleep(0.5)

# rodape
print()
print('=-' * 20, '\n')