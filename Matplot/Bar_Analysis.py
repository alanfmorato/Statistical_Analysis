import matplotlib.pyplot as plt

x = ['python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']

y = [10, 8, 6, 4, 2, 1]

plt.figure(figsize=(10,5))#Definindo tamanho da figura

plt.title("Programming Language usage")#Definindo título

plt.ylabel('Usage')#Definindo título do eixo y

plt.xlabel('Language')#Definindo título do eixo x

plt.bar(x,y, color= 'mediumpurple', alpha=.6)#Definindo tipo de gráfico, cor e transparência

plt.show()#exibindo gráfico

plt.title("Programming Language usage")#Definindo título

plt.ylabel('Usage')#Definindo título do eixo y

plt.xlabel('Language')#Definindo título do eixo x

plt.barh(x,y, color= 'mediumpurple', alpha=.6)#Definindo tipo de gráfico, cor e transparência

plt.show()#exibindo gráfico