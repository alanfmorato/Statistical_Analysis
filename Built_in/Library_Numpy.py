import numpy as np

array1 = np.zeros(shape=(6,6))#Definindo uma matriz 6x6 de zero

array2 = np.ones(shape=(4,4))#Definindo uma matriz 4x4 de 1

array1[1:5, 1:5] = np.ones(shape=(4,4))#Substituindo o meio (4x4) da matriz por 1

array3 = np.full(shape=(2,2), fill_value=2)#Definindo uma matriz 2x2 de 2

array1[2:4, 2:4] = np.full(shape=(2,2), fill_value=2)#Substituindo o meio (2x2) da matriz por 2

print(array1.ndim)#Dimensão da matriz
print("-"*15,"//","-"*15)
print(array1.shape)#matriz(x,x)
print("-"*15,"//","-"*15)
print(array1.size)#Quantidade de itens
print("-"*15,"//","-"*15)
print(array1)#Matriz final
print("-"*15,"//","-"*15)


