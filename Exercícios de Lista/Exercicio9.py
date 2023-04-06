#Exercício 9:
print('Exercício 9:')
VetorA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calcularSomaDosQuadrados(listaDeInteiros):
    somaDosQuadrados = 0
    for i in listaDeInteiros:
        somaDosQuadrados += i * i
    return somaDosQuadrados

print('Lista de inteiros: ' + str(VetorA))
print('Soma dos Quadrados: ' + str(calcularSomaDosQuadrados(VetorA)))
