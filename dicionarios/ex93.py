# cabecalho
print('=-' * 20)
print(f'{"Desafio 92":^40}')
print('-' * 40)
print()

jogador = {
    'nome': str(input('Digite o nome do jogador: ')),
    'partidas': []
}

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, partidas):
    jogador['partidas'].append(
        int(input(f'    -> Quantos gols na partida {c}? '))
    )
jogador['total'] = sum(jogador['partidas'])
print()

print(jogador)
print('-' * 40)


# rodape
print()
print('=-' * 20, '\n')