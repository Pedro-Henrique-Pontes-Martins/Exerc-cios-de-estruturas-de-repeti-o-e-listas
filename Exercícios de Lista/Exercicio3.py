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
