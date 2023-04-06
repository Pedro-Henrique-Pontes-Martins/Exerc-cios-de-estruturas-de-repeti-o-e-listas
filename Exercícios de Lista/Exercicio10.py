#Exercício 10:
print('Exercício 10:')
vetor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetor3 = []

contador = 0
for i in vetor1:
    vetor3.append(i)
    vetor3.append(vetor2[contador])
    contador += 1
print(vetor3)
