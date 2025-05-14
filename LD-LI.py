import numpy as np 

#Informar tamano da matriz
print("Digite o tamanho da sua matriz:")
x = int(input("Linhas: "))
y = int(input("Colunas: "))

#se existir mais colunas do que linhas, então as colunas de A são LD
if(y > x):
    print("A sua matriz é LD(Linearmente Dependente)")
    exit()

#vetor vazio
matrizP = []
for i in range(x):  #for para as linhas da matriz
    vetorAux = []
    for c in range(y):  #for para as colunas da matriz
        print("Digite o valor da posicao ["+str(i)+","+str(c)+"]:") #Pede o valor de cada posição
        k = int(input("->"))
        vetorAux.append(k) #adiciona ao vetor das linhas
    matrizP.append(vetorAux) #adiciona os vetores a nossa matrix

matrizP = np.array(matrizP) #transforma a matrix em um array nump

matrizAux = []
for i in range(x): #cria a matrix com todos os elementos
    matrizAux.append([0]) #[[0],[0],[0],....]

matrizAux = np.array(matrizAux) #transforma a matrix em um array nump

try: # pega o possivel erro de solução onde nosso sistema, tem varias soluções
    solution = np.linalg.solve(matrizP, matrizAux) # tenta solucionar o sistema e retorna a solução
    print("Os vetores são LI(Linearmente Independente): ",solution)

except np.linalg.LinAlgError: # caso tenha mais de uma solução o sistema é LD
    print("Os vetores dos coeficientes é LD(Linearmente Dependente).")

