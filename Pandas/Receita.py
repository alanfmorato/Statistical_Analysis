import numpy as np
import pandas as pd

ingredientes = ['maisena', 'manteiga', 'ovos', 'salsicha', 'maça']

ingredientes = np.array(ingredientes)

ingredientes = pd.Series(ingredientes)

ingredientes.name = 'ingredientes'

quantidades = pd.Series(data=[200, 150, 5, 1, 6], index=ingredientes.values, name='quantidades', dtype=float)

quantidades = quantidades.reset_index(drop=True)

dataframe = pd.concat([ingredientes, quantidades], axis=1, ignore_index=True)

dataframe.columns = ['Ingredientes', 'Quantidades']

#print(ingredientes)

print(dataframe)