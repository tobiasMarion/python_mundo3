# cabecalho
print('=-' * 20)
print(f'{"Desafio 83":^40}')
print('-' * 40)

expressao = input('Digite uma expressão:')

quantidade = expressao.count('(') == expressao.count(')')

abrir = None
fechar = None
certo = False 

if expressao.count('(') == 0 and quantidade:
    certo = True


if not(certo):
    for i, caracter in enumerate(expressao):
        if caracter == '(':
            abrir = i
        elif caracter == ')':
            fechar = i
        if fechar == None or abrir < fechar:
            certo = True

if (certo):
    print('ta certo')
else:
    print('Errado')


# rodape
print('\n')
print('=-' * 20, '\n')