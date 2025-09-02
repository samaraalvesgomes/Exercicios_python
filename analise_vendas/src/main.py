'''Objetivo do exercício:
    Ler o arquivo vendas_loja.csv
    Filtrar os produtos cuja quantidade vendida seja maior ou igual a 5
    Calcular o valor médio do preço unitário desses produtos filtrados
    Salvar o resultado em um arquivo texto, algo como:
"O preço médio dos produtos com vendas maiores que 5 unidades é R$ XX,XX"'''

import pandas as pd
import numpy as np

#Ler o arquivo vendas_loja.csv

vendas_df = pd.read_csv('data/vendas_loja.csv')
print(vendas_df)  

#Filtrar os produtos cuja quantidade vendida seja maior ou igual a 5
filtro = vendas_df.loc[vendas_df['quantidade'] >= 5]
print(filtro)

#Calcular o valor médio do preço unitário desses produtos filtrados
preco_medio = np.mean(filtro['preco_unitario'])
print(preco_medio)

#Salvar o resultado em um arquivo texto
with open('data/preco_medio.txt', 'w') as arquivo:
    arquivo.write(f'O preço médio dos produtos com vendas maiores que 5 unidades é R$ {preco_medio:.2f}')