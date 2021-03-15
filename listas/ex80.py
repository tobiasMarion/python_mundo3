# cabecalho
print('=-' * 20)
print(f'{"Desafio 78":^40}')
print('-' * 40)

lista = []

for c in range(0, 5):
    num = int(input('Digite um número: '))

    if c == 0:
        print('Valor adicionado ao final da lista')
        lista.append(num)
    else:
        if num in lista:
            print('Valor já foi adicionado')
        else:
            if num > max(lista):
                lista.append(num)
                print('Valor adicionado ao final da lista')
            else:
                for pos, valor in enumerate(lista):
                    if num < valor:
                        lista.insert(pos, num)
                        print(f'Valor adicionado na posição {pos}')
                        break
                
print(f'Os valores digitados foram: {lista}')

# rodape
print('\n')
print('=-' * 20, '\n')
