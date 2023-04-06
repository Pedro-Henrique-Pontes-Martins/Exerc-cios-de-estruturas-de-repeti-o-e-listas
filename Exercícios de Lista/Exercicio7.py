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