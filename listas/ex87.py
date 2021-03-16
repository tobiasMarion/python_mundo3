# cabecalho
print('=-' * 20)
print(f'{"Desafio 87":^40}')
print('-' * 40)
print()

matriz = [[], [], []]
somaPares = 0
soma3coluna = 0

for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite o valor para a posição [{x:^3}][{y:^3}]: '))
        
        if num % 2 == 0:
            somaPares += num

        if y == 2:
            soma3coluna += num

        matriz[x].append(num)

print('-' * 40, '\n')

for linha in matriz:
    for coluna in linha:
        print(f'[{coluna:^5}]', end=' ')
    print()
print()

print(f'A soma dos valores pares digitados é: {somaPares}.')
print(f'A soma dos valores da terceira coluna é: {soma3coluna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')

# rodape
print()
print('=-' * 20, '\n')