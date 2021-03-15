# cabecalho
print('=-' * 20)
print(f'{"Desafio 78":^40}')
print('-' * 40)

lista = []

for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))

maior = max(lista)
maxLista = []

menor = min(lista)
minLista = []

for i, n in enumerate(lista):
    if n == maior:
        maxLista.append(i)
    elif n == menor:
        minLista.append(i)

print(f'=> Os números digitados foram: {lista}.')
print(f'=> O maior número é {maior} e está nas posições: {maxLista}.')
print(f'=> O maior número é {menor} e está nas posições: {minLista}.')


# rodape
print('\n')
print('=-' * 20, '\n')