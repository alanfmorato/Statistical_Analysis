import numpy as np
import matplotlib.pyplot as plt

meses = np.array(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set'])

temperaturas = np.array([29, 28, 27, 22, 24, 21, 20, 18, 15])

plt.figure(figsize=[5, 5])#Tamanho da figura

plt.title('Meses x Temperaturas')#Título do gráfico

plt.bar(meses, temperaturas, label='Temperaturas')#Eixo x, Eixo y e legenda

plt.yticks([0, 10, 20, 30])#Intervalor do eixo y

plt.xlabel('Meses')#Rotulo do eixo x

plt.ylabel('Temperatura')#Rotulo do eixo y

plt.legend(loc=0)#Legenda

plt.show()#Mostrar gráfico

plt.savefig('Meses X Temperatura')