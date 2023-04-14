index = 0
while (index == 0):
    print('Registre seu nome de usuário:')
    usuário = input()
    print('Registre sua Senha:')
    senha = input()
    if senha == usuário:
        print('Senha Inválida. A senha deve ser diferente do usuário.')
    else:
        index = 1