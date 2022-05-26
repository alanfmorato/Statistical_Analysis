import numpy as np

mes = np.arange(1, 29).reshape(4, 7)#Definindo um array de 28 dias e separando em 4 semanas

calendario = np.tile(mes, (12, 1, 1)) #Definindo 12 meses

calendario = calendario.astype(str) #Definindo o fim de semana como w
calendario[:, :, 5:7] = 'W'

calendario = calendario.astype(str) #Definindo o inicio da semana como s
calendario[:, 0:1, 0:1] = 'S'

calendario = calendario.astype(str) #Definindo o inicio da semana como s
calendario[:, 3:4, 6:7] = 'E'

dias = np.array([1, 15, 21, 1, 7, 12, 2, 15, 25])#Dias dos feriados

meses = np.array([1, 4, 4, 5, 9, 10, 11, 11, 12])#Meses dos feriados

meses = meses - 1

dias_semana = (dias - 1) % 7#transformando em posições da matriz

semana_mes = (dias-1)//7#descobrindo em qual semana do mês é

calendario[meses, semana_mes, dias_semana] = 'F' #Definindo feriados

calendario[~np.isin(calendario,['S', 'W', 'E', 'F'])] = 'D'#Definindo disas uteis

print(calendario.shape)
print("*"*80)
print(calendario)
print("*"*80)