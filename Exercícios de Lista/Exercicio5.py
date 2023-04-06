#Exercício 5:
print("Exercício 5:")
Lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ListaPar = []
ListaImpar = []
for i in Lista5:
    if(Lista5[i-1]%2):
        ListaImpar.append(Lista5[i-1])
    else:
        ListaPar.append(Lista5[i-1])

print(Lista5)
print(ListaPar)
print(ListaImpar)