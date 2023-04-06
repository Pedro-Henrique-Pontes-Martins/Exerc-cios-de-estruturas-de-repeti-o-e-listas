#Exercício 6:
print('Exercício 6:')
Aluno1 = [7, 4, 8, 10]
Aluno2 = [7, 4, 9, 1]
Aluno3 = [6, 5, 9, 1]
Aluno4 = [10, 10, 9, 9]
Aluno5 = [4, 1, 1, 10]
Aluno6 = [10, 10, 10, 10]
Aluno7 = [3, 6, 7, 8,]
Aluno8 = [10, 4, 7, 1]
Aluno9 = [8, 8, 8, 1,]
Aluno10 = [8, 2, 9, 1]
AllAlunos = [Aluno1, Aluno2, Aluno3, Aluno4, Aluno5, Aluno6, Aluno7, Aluno8, Aluno9, Aluno10]

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
        médiasDosAlunos.append(calcularMédia(i))
    return médiasDosAlunos

def númeroDeAlunosAprovados(listaDeNotas):
    AlunosAprovados = []
    for i in calcularMédiasDosAlunos(listaDeNotas):
        if i >= 7:
            AlunosAprovados.append(i)
    númeroDeAlunosAprovados = len(AlunosAprovados)
    return númeroDeAlunosAprovados

print('Médias dos Alunos: ' + str(calcularMédiasDosAlunos(AllAlunos)))
print('Número de Alunos Aprovados: ' + str(númeroDeAlunosAprovados(AllAlunos)))
