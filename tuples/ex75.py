# cabecalho
print('=-' * 20)
print(' ' * 15, 'Desafio 72', ' ' * 15)
print('=-' * 20, '\n')

numeros = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais número: ')),
    int(input('Digite o último número: '))
)

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 9 foi digitado {numeros.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in numeros: 
    if n % 2 == 0:
        print(n, end=' ')

# rodape 
print('\n', '=-' * 20, '\n')