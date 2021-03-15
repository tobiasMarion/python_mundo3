# cabecalho
print('=-' * 20)
print(f'{"Desafio 78":^40}')
print('-' * 40)

lista = []
dado = []

while True:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))

    lista.append(dado[:])
    dado.clear()

    while True:
        dnv = input('Quer digitar outro número? [S/N]').lower()
        if dnv in 'sn':
            break
    if dnv == 'n': 
        break

pesado = [[], 0]
leve = [[], 0]

for pos, pessoa in enumerate(lista):
    if pos == 0:
        pesado[0].append(pessoa[0])
        pesado[1] = pessoa[1]
        leve[0].append(pessoa[0])
        leve[1] = pessoa[1]
    else:
        if pessoa[1] > pesado[1]:
            pesado[0] = [pessoa[0]]
            pesado[1] = pessoa[1]

        elif pessoa[1] == pesado[1]:
            pesado[0].append(pessoa[0])

        elif pessoa[1] < leve[1]:
            leve[0] = [pessoa[0]]
            leve[1] = pessoa[1]

        elif pessoa[1] == leve[1]:
            leve[0].append(pessoa[0])
    print(pessoa[0], end=' ')
    
print(f'Ao todo, você cadastrou {len(lista)} pessoas')
print(f'As pessoas mais pesadas foram {pesado[0]} com {pesado[1]} kg')
print(f'As pessoas mais leves foram {leve[0]} com {leve[1]} kg')

# rodape
print('\n')
print('=-' * 20, '\n')