n1 = [1, 2, 3, 10, 5]
index = 0
soma = 0
média = 0

while(index != len(n1)):
    soma += n1[index]
    index += 1
média = soma/len(n1)

print('Resultado da soma: ' + str(soma))
print('Resultado da média: ' + str(média))