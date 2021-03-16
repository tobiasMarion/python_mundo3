from datetime import datetime

# cabecalho
print('=-' * 20)
print(f'{"Desafio 92":^40}')
print('-' * 40)
print()

trabalhador = {
    'nome': str(input('Nome: ')),
    'idade': datetime.now().year - int(input('Ano de nascimento: ')),
    'carteira': int(input('Carteira de trabalho: '))
}

if trabalhador['carteira'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Valor do salário: '))
    trabalhador['aposentadoria'] = (trabalhador['contratacao'] + 35) - (datetime.now().year - trabalhador['idade'])
print()

for k, v in trabalhador.items():
    print(f'{k} tem valor {v}')

# rodape
print()
print('=-' * 20, '\n')