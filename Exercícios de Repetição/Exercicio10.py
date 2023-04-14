print('Digite um número')
primeiroNúmero = int(input())
print('Digite outro número')
segundoNúmero = int(input())

print('Números entre os números digitados:')
while (primeiroNúmero != segundoNúmero):
    primeiroNúmero += 1
    if(primeiroNúmero != segundoNúmero):
        print(primeiroNúmero)