# cabecalho
print('=-' * 20)
print(f'{"Desafio 82":^40}')
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

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('Os números digitados foram:', lista)
print('Dentre eles os pares são:', pares)
print('Já os ímpares são:', impares)

# rodape
print('\n')
print('=-' * 20, '\n')