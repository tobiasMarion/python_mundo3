# cabecalho
print('=-' * 20)
print(' ' * 15, 'Desafio 72', ' ' * 15)
print('=-' * 20)
print('')

extenso = (
    'zero', 'um', 'dois',
    'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove',
    'dez', 'onze',
    'doze', 'treze',
    'quatorze', 'quinze',
    'dezesseis', 'dezessete',
    'dezoito', 'dezenove',
    'vinte'
)

while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))

        if 0 <= numero <= 20: break
        else: print('Tente novamente.', end=' ')

    print(f'Você digitou o número {extenso[numero]}.')

    while True:
        dnv = input('Você quer tentar novamente? [S/N] ').lower()
        if dnv == 's' or dnv == 'n': break
    if dnv == 'n': break

# rodape 
print('=-' * 20)
print('')