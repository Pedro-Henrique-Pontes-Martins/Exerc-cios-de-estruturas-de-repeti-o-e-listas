print('Digite a população da cidade A')
populaçãoA = float(input()) 
print('Digite o valor, em porcentagem, da taxa de crescimento da cidade A')
taxaDeCrescimentoDaPopulaçãoA = float(input())/100
taxaDeCrescimentoDaPopulaçãoA += 1
print('Digite a população da cidade B')
populaçãoB = float(input()) 
print('Digite o valor, em porcentagem, da taxa de crescimento da cidade B')
taxaDeCrescimentoDaPopulaçãoB = float(input())/100
taxaDeCrescimentoDaPopulaçãoB += 1
númeroDeAnos = 0

while (populaçãoB > populaçãoA):
        populaçãoA *= taxaDeCrescimentoDaPopulaçãoA
        populaçãoB *= taxaDeCrescimentoDaPopulaçãoB
        númeroDeAnos += 1
print ('A população da cidade A levará ' + str(númeroDeAnos) + ' anos para alcançar a da cidade B') 