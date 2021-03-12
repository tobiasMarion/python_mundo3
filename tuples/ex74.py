from random import randint

# cabecalho
print('=-' * 20)
print(' ' * 15, 'Desafio 74', ' ' * 15)
print('=-' * 20)
print('')

numeros = (
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10)
)

print(f'Eu sorteei os números {numeros}')
print(f'O maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')

# rodape 
print('=-' * 20)
print('')