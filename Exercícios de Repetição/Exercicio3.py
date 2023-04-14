contador = 0
while(contador == 0):
    print('Digite o seu nome:')
    nome = input()
    if len(nome) < 3:
        print('Nome Inválido. O nome deve conter no mínimo 3 caracteres.')
    else:
        contador = 1

contador = 0
while(contador == 0):
    print('Digite o sua idade:')
    idade = int(input())
    if idade > 0 and idade < 150:
        contador = 1
    else:
        print('Idade Inválida.')

contador = 0
while(contador == 0):
    print('Digite o seu salário:')
    salário = int(input())
    if salário > 0:
        contador = 1
    else:
        print('Salário Inválido.')

contador = 0
while(contador == 0):
    print("Digite o seu sexo ('F' ou 'M'):")
    sexo = input()
    if sexo == 'F' or sexo == 'M':
        contador = 1
    else:
        print('Informação Inválida.')

contador = 0
while(contador == 0):
    print("Digite o seu Estado Civil ('S', 'C' 'V' ou 'D'):")
    estadoCivil = input()
    if estadoCivil == 'S' or estadoCivil == 'C' or estadoCivil == 'V' or estadoCivil == 'D':
        contador = 1
    else:
        print('Informação Inválida.')