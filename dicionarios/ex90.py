# cabecalho
print('=-' * 20)
print(f'{"Desafio 90":^40}')
print('-' * 40)
print()

aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))
print()

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'

elif aluno['media'] < 5:
    aluno['situacao'] = 'REPROVADO'

else:
    aluno['situacao'] = 'RECUPERAÇÃO'

for k, v in aluno.items():
    print(f'   => {k} é igual a {v}')


# rodape
print()
print('=-' * 20, '\n')