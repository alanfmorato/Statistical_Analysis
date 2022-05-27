import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

amostras=1000

seed = 0
np.random.seed(seed)#Gerando uma semente aleatória

idade = np.random.randint(0, 101, amostras)#Gerando idades aleatórias

jan2000 = pd.date_range(start='2000/01/01', end='2000/01/31')#Gerando datas de nascimento aleatórias em um range

array = np.random.choice(jan2000, amostras)#Gerando a quantidade de datas de nascimento necessárias

notas = np.random.uniform(0, 1000, amostras)#Gerando a quantidade de notas necessárias

sexo = np.random.choice(['M', 'F'], amostras)#Gerando sexo aleatoriamente

estados = [
'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'] #Atribuindo estados aleatoriamente


df = pd.DataFrame({
    'idade': np.random.randint(0, 101, amostras),
    'data': np.random.choice(jan2000, amostras),
    'nota': np.random.uniform(0, 1000, amostras),
    'sexo': np.random.choice(['M', 'F'], amostras),
    'estado': np.random.choice(estados, amostras)
})

faltantes_ix = df.sample(frac=0.2, random_state=seed).index#Pegando 20% dos valores

df.loc[faltantes_ix, 'nota'] = np.nan#Pegando 20% dos valores e definindo nota nan

df = df.fillna(value=0)#Pegando 20% dos valores e definindo nota nula

gt_80 = df['idade'] > 80
lt_18 = df['idade'] < 18

inconsistencia = gt_80 | lt_18

df = df[~inconsistencia]#Filtrando as pessoas maiores que 80 anos e menores que 18

df['dia da semana'] = df.data.dt.weekday#Definindo coluna da semana com o dia da data

df['aprovado'] = df['nota'] >= 600#verificando quem foi aprovado

mapa = {
    0: 'Segunda',
    1: 'Terça',
    2: 'Quarta',
    3: 'Quinta',
    4: 'Sexta',
    5: 'Sábado',
    6: 'Domingo'
}

df['dia da semana'] = df['dia da semana'].map(mapa)#Definindo dia da semana como palavras

pd.crosstab(df.estado, df.sexo, margins=True, margins_name='total')#Cruzando a tabela estado e sexo

aprovados_sexo = df[df['aprovado']].sexo.value_counts()#Verificando quantidade de aprovados por sexo

plt.figure(figsize=(6, 4))

plt.pie(aprovados_sexo, autopct='%.2f%%', explode=[.1, 0], shadow=.8)#plotando o gráfico de pizza de aprovados por sexo

plt.title('Aprovados por sexo')

plt.legend(labels=['M', 'F'])#definindo legenda

plt.show()

aprovados_estado = df[df['aprovado']].estado.value_counts().sort_values(ascending=True)#Definindo aprovados por estado

plt.figure(figsize=(8, 6))

plt.title('Aprovados por estado')#Titulo

plt.ylabel('Aprovados')#Definindo título do eixo y

plt.xlabel('Estados')#Definindo título do eixo x

plt.bar(estados, aprovados_estado, color= 'mediumpurple', alpha=.6)#Definindo tipo de gráfico

plt.show()

sns.scatterplot(data=df, x='idade', y='nota', hue='sexo')#Definindo tipo de gráfico

plt.show()

plt.figure(figsize=(10,6))

df['dia da semana'].value_counts().plot(kind='bar')#Definindo tipo de gráfico

plt.title('Participação')

plt.show()

df['data'].value_counts().plot(kind='line')#Definindo tipo de gráfico

plt.title('Participação')

plt.show()

sns.stripplot(data=df, x='dia da semana', y='nota')#Definindo tipo de gráfico

plt.show()

df.sort_values('nota', ascending=False).iloc[:100].to_csv('Top100.csv')#Salvando em arquivo CSV