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
def calcularNotas(Lista):
    numeroDeNotas = len(Lista)
    média = sum(Lista) / numeroDeNotas
    return média
print('Média:')
print(calcularNotas(Lista3))

#Exercício 4:
Lista4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def quantidadeDeConsoantes(Lista4):
    consoantes = 0
    contador = 0
    for i in Lista4:
        if (Lista4[contador] != "a" or Lista4[contador] != "e" or Lista4[contador] != "i" or Lista4[contador] != "o" or Lista4[contador] != "u"):
            consoantes += 1
        contador += 1
    return consoantes
print('Quantidade de consoantes:')
print(quantidadeDeConsoantes(Lista4))