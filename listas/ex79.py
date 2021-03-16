# cabecalho
print('=-' * 20)
print(f'{"Desafio 79":^40}')
print('-' * 40)

lista = []

while True:
    num = int(input('Digite um número: '))
    
    if num in lista:
        print('Valor duplicado. Não vou adicionar novamente. ')
    else:
        lista.append(num)
        print('Valor adicionado. ')

    while True:
        dnv = input('Quer digitar outro número? [S/N] ').lower()

        if dnv not in 'ns':
            continue
        else:
            break

    if dnv == 'n': 
        break    

print('\nOs números digitados foram:', lista)

# rodape
print('\n')
print('=-' * 20, '\n')
