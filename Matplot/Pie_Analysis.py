import matplotlib.pyplot as plt

valores = [15, 30, 45, 10]

rotulos = ['Apple', 'Banana', 'Orange', 'Pineapple']#Definindo legendas

explode = [.1, .1, .1, .1]#Definindo explosão do gráfico


plt.figure(figsize=[5,5])#Definindo tamanho da imagem


plt.pie(valores, explode=explode, labels=rotulos, colors=['blue', 'orange', 'green', 'red'], autopct='%.1f%%', shadow=True, startangle=90)#Definindo o gráfico de pizza

plt.show()#Exibindo o gráfico

