#Exercício 6:
print('Exercício 6:')

Alunos = [['Roger', [7, 4, 8, 10]], ['Lucas', [7, 4, 9, 1]], ['Pedro', [10, 10, 9, 9]], ['Mateus', [6, 5, 9, 1]], ['Miguel', [4, 1, 1, 10]], ['Deividi', [10, 10, 10, 10]], ['Henrique', [3, 6, 7, 8,]], ['Cauã', [10, 4, 7, 1]], ['Davi', [8, 8, 8, 1, 10] ], ['Gustavo', [8, 2, 9, 1,] ] ]

def calcularMédia(Lista):
    numeroDeNotas = len(Lista)
    soma = 0
    for i in Lista:
        soma = soma + i
    média = soma / numeroDeNotas
    return média

def calcularMédiasDosAlunos(listaDeNotas):
    médiasDosAlunos = []
    for i in listaDeNotas:
        médiasDosAlunos.append([i[0], calcularMédia(i[1])])
    return médiasDosAlunos

def exibirMédias(listaDeNotas):
    for i in calcularMédiasDosAlunos(listaDeNotas):
        print(i[0] + ': ' + str(i[1]))

def númeroDeAlunosAprovados(listaDeNotas):
    AlunosAprovados = []
    for i in calcularMédiasDosAlunos(listaDeNotas):
        if i[1] >= 7:
            AlunosAprovados.append(i)
    númeroDeAlunosAprovados = len(AlunosAprovados)
    return númeroDeAlunosAprovados

print('Médias dos Alunos:')
exibirMédias(Alunos)
print('Número de Alunos Aprovados: ' + str(númeroDeAlunosAprovados(Alunos)))
