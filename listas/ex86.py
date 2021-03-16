# cabecalho
print('=-' * 20)
print(f'{"Desafio 86":^40}')
print('-' * 40)
print()


matriz = [[], [], []]

for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite o valor para a posição [{x:^3}][{y:^3}]: '))
        matriz[x].append(num)

print('-' * 40, '\n')

for linha in matriz:
    for coluna in linha:
        print(f'[{coluna:^5}]', end=' ')
    print()
    
# rodape
print()
print('=-' * 20, '\n')