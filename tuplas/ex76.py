# cabecalho
print('=-' * 20)
print(f'{"Desafio 76":^40}')
print('=-' * 20)

produtos = (
    'Mouse', 250,
    'Teclado', 400,
    'Monitor', 1200,
    'Memória Ram', 300,
)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>8.2f}')


# rodape
print('\n')
print('=-' * 20, '\n')
