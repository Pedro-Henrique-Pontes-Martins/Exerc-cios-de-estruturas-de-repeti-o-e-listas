#Exercício 4:
print('Exercício 4:')
Lista4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
ListaVogais = ["a","e","i","o","u"]
def quantidadeDeConsoantes(Lista4):
    consoantes = 0
    contador = 0
    for i in Lista4:
        if not Lista4[contador] in ListaVogais:
            consoantes += 1
        contador += 1
    return consoantes
print('Quantidade de consoantes:')
print(quantidadeDeConsoantes(Lista4))