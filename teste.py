import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import math

#carregando o dataframe total
df_inicial = pd.read_csv("healthcare-dataset-stroke-data.csv")
l= [0.4371549704082704, 0.028841943737234352, 0.028312439197258368, 0.21058274702738347, 0.15342491852730977, 0.0, 0.024384420789903775, 0.00957712911325327, 0.0, 0.0, 0.0, 0.007707867324799797, 0.0, 0.0, 0.007707867324799797, 0.006494067989533142, 0.006494067989533129, 0.03060064912821328, 0.03830851645301308, 0.010408394989494392]


def return_most_important_features(lista_features, df):
    lista_ids = []
    for i in range(2):
        maior = -math.inf
        id_maior = 0
        for feature in range(len(lista_features)):
            if lista_features[feature] > maior:
                maior = lista_features[feature]
                id_maior = feature
        lista_features[id_maior] = 0
        lista_ids.append(id_maior)
    l1 = df.columns[lista_ids[0]]
    l2 = df.columns[lista_ids[1]]
    return (l1,l2)

print(return_most_important_features(l,df_inicial))