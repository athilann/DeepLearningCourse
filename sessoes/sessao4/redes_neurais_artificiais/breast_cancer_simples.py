import pandas as pd

import os
current_directory = os.getcwd()
print(current_directory) 

previsores = pd.read_csv(current_directory+'/sessoes/sessao4/redes_neurais_artificiais/entradas-breast.csv')
classe = pd.read_csv(current_directory+'/sessoes/sessao4/redes_neurais_artificiais/saidas-breast.csv')

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe,test_size=0.25)

