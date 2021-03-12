# cabecalho
print('=-' * 20)
print(' ' * 15, 'Desafio 73', ' ' * 15)
print('=-' * 20)
print('')

times = (
    'Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo',
    'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
    'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians',
    'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza',
    'Vasco', 'Goiás', 'Coritiba', 'Botafogo'
)

print(f'Os times são: {times}')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O Grêmio está na posição: {times.index("Grêmio") + 1}°')


# rodape 
print('=-' * 20)
print('')