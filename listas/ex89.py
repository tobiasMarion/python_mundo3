# cabecalho
print('=-' * 20)
print(f'{"Desafio 89":^40}')
print('-' * 40)
print()

alunos = []

while True:
    dado = ['', []]
    dado[0] = (str(input('Digite o nome do aluno: ')))
    for c in range(1, 3):
        dado[1].append(float(input(f'Digite a {c}º nota: ')))

    alunos.append(dado[:])
    dado.clear()

    while True:
        dnv = input('Quer cadastrar outro usuário? [S/N] ').lower()
        if dnv in 'sn':
            break
    if dnv == 'n': 
        break
print()

print(f'{"Nº":<5} {"NOME":<20} {"NOTA":<5}')
print('-' * 40)
for c, aluno in enumerate(alunos):
    media = sum(aluno[1]) / 2
    print(f'{c:<5} {aluno[0]:<20} {media:<5.2f}')
print()


while True:
    opcao = int(input('Mostrar notas de qual aluno? [999 interrompe] '))

    if opcao == 999:
        break
    else:
        aluno = alunos[opcao]
        print(f'As notas de {aluno[0]} são: {aluno[1]}.')
        print()

# rodape
print()
print('=-' * 20, '\n')