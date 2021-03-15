# cabecalho
print('=-' * 20)
print(f'{"Desafio 77":^40}')
print('-' * 40)

palavras = (
    'Python', 'Javascript', 
    'Go', 'Java', 
    'ruby', 'Pascal', 
    '.NET', 'Lua'
)

vogais = 'aeiou'

for palavra in palavras:
    print(f'A palavra {palavra} contém as vogais:', end=' ')
    for vogal in vogais:
        if vogal in palavra.lower():
            print(vogal, end=' ')
    print('')

# rodape
print('\n')
print('=-' * 20, '\n')