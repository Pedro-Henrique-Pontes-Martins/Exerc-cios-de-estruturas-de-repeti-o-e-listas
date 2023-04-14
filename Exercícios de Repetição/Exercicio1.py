index = 0
while(index == 0):
    print('Me informe uma nota entre 0 e 10:')
    valorInformado = int(input())
    if valorInformado >= 0 and valorInformado <= 10:
        index = 1
    else:
        print('Valor Inválido')