print('Digite um número:')
primeiroNúmero = int(input())
print('Digite outro número:')
segundoNúmero = int(input())

print('Números entre os números digitados:')
if (primeiroNúmero < segundoNúmero):
    while (primeiroNúmero != segundoNúmero):
        primeiroNúmero += 1
        if(primeiroNúmero != segundoNúmero):
            print(primeiroNúmero)
else:
    while (segundoNúmero != primeiroNúmero):
        segundoNúmero += 1
        if(segundoNúmero != primeiroNúmero):
            print(segundoNúmero)