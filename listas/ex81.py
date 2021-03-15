# cabecalho
print('=-' * 20)
print(f'{"Desafio 78":^40}')
print('-' * 40)

lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        dnv = input('Quer digitar outro número? [S/N]').lower()
        if dnv in 'sn':
            break
    if dnv == 'n': 
        break
 
print(f'Foram digitados {len(lista)} números')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')

if 5 in lista:
    print(f'O valor 5 está na lista')
else:
    print(f'O valor 5 não está na lista')

# rodape
print('\n')
print('=-' * 20, '\n')