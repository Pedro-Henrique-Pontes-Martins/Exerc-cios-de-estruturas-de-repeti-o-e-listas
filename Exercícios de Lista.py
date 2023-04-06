#Exercício 1:
print('Exercício 1:' )
Lista1 = [1, 2, 3, 4, 5]
print(Lista1)

#Exercício 2:
print('Exercício 2:')
Lista2 = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
print(Lista2)
Lista2.reverse()
print(Lista2)

#Exercícios 3:
print('Exercício 3:')
Lista3 = [10,10,10,10]
print(Lista3)
def calcularMédia(Lista):
    numeroDeNotas = len(Lista)
    soma = 0
    for i in Lista:
        soma = soma + i
    média = soma / numeroDeNotas
    return média
print('Média: ' + str(calcularMédia(Lista3)))

#Exercício 4:
print('Exercício 4:')
Lista4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
ListaVogais = ["a","e","i","o","u"]
def quantidadeDeConsoantes(Lista4):
    consoantes = 0
    contador = 0
    for i in Lista4:
        if not Lista4[contador] in ListaVogais:
            consoantes += 1
        contador += 1
    return consoantes
print('Quantidade de consoantes:')
print(quantidadeDeConsoantes(Lista4))

#Exercício 5:
print("Exercício 5:")
Lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ListaPar = []
ListaImpar = []
for i in Lista5:
    if(Lista5[i-1]%2):
        ListaImpar.append(Lista5[i-1])
    else:
        ListaPar.append(Lista5[i-1])

print(Lista5)
print(ListaPar)
print(ListaImpar)

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

#Exercício 7:
print('Exercício 7:')
ListaEx7 = [4, 7, 8, 3, 5]

def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def multiplicação(lista):
    multiplicação = 1
    for i in lista:
        multiplicação *= i
    return multiplicação

print('Lista: ' + str(ListaEx7))
print('Soma dos Valores da Lista: ' + str(soma(ListaEx7)))
print('Multiplicação dos Valores da Lista: ' + str(multiplicação(ListaEx7)))

#Exercício 8:
listaDeIdades = []
listaDeAlturas = []
for i in range(0, 5):
    print('Insira uma idade')
    idade = input()
    print('Insira uma altura em metros')
    altura = input()
    listaDeIdades.append(idade)
    listaDeAlturas.append(altura)

listaDeIdades.reverse()
listaDeAlturas.reverse()

contador = 0
for i in listaDeIdades:
    print('Pessoa ' + str(contador + 1) + ':' )
    print('Idade: ' + str(i))
    print('Altura: '+ str(listaDeAlturas[contador]))
    contador += 1

