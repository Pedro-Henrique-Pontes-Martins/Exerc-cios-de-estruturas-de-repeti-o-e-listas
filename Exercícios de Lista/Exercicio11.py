#Exercício 11:
print('Exercício 11:')
vetor4 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
vetor5 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
vetor6 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
vetor7 = []

contador = 0
for i in vetor4:
    vetor7.append(i)
    vetor7.append(vetor5[contador])
    vetor7.append(vetor6[contador])
    contador += 1
print(vetor7)