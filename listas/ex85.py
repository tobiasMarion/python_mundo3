# cabecalho
print('=-' * 20)
print(f'{"Desafio 85":^40}')
print('-' * 40)

lista = [[], []]

for c in range(1,8):
    num = int(input(f'Digite o {c}º valor: '))
    lista[num % 2].append(num)

sorted(lista[0])
sorted(lista[1])

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')

# rodape
print('\n')
print('=-' * 20, '\n')