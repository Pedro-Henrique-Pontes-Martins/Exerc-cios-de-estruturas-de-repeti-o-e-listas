#Exercício 8:
print('Exercício 8:')
listaDeIdades = []
listaDeAlturas = []
for i in range(0, 5):
    print('Insira uma idade')
    idade = input()
    print('Insira uma altura em metros')
    altura = input()
    listaDeIdades.append(idade)
    listaDeAlturas.append(altura)

listaDeIdades.reverse()
listaDeAlturas.reverse()

contador = 0
for i in listaDeIdades:
    print('Pessoa ' + str(contador + 1) + ':' )
    print('Idade: ' + str(i))
    print('Altura: '+ str(listaDeAlturas[contador]))
    contador += 1 
