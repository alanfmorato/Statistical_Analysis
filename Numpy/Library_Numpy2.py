import numpy as np

array1 = np.arange(81).reshape(9,9)#Criando um array e transformando em uma matriz 9x9

mask_impar = array1 % 2 == 1 #Verificando se é impar

mask_par = array1 % 2 == 0 #Verificando se é par

mask_sete = array1 % 7 == 0 #Verificando multiplos de sete


print(array1)
print("*"*80)
print(array1[mask_impar])
print("*"*80)
print(array1[mask_par])
print("*"*80)
print(array1[mask_sete])
print("*"*80)
print(array1.diagonal())#Mostrando a diagonal da matriz