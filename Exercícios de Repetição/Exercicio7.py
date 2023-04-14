n1 = [1, 2, 3, 10, 5]
maiorNumero = 0
index = 0
while(index != len(n1)):
    if(maiorNumero < n1[index]):
        maiorNumero = n1[index]
    index += 1
print('O maior número é: ' + str(maiorNumero))