import matplotlib.pyplot as plt
import numpy as np

x=[.8, 2.4, 3.5, 4.9, 6.7, 7.1]

y=[20, 14, 12, 28, 35, 22]

tamanho = [100, 60, 20, 80, 20, 100] #Definindo valore de tamanho das "bolinhas"

cores = ['red', 'green', 'yellow', 'yellow', 'black', 'blue'] #Definindo cores das "bolinhas"

plt.figure(figsize=(10, 5))#Definindo o tamanho da figura

plt.scatter(x, y, s=tamanho, c=cores)#definindo tipo de gráfico

plt.xticks(np.arange(0, 7.5, 0.5))#Intervalo x

plt.yticks(np.arange(0, 40, 5))#Intervalo y

plt.show()#exibindo gráfico