#IMPORT DA BIBLIOTECA PANDAS PARA MANIPULAÇÃO E ANÁLISE DE DADOS
import pandas as pd

#IMPORT PARA A GERAÇÃO DE GRAFICOS
import matplotlib.pyplot as plt

#LER O ARQUIVO "Stores.csv" NA PASTA
df = pd.read_csv("Stores.csv")

#RENOMEAR TODAS AS COLUNAS DO ARQUIVO
df = df.rename(columns={
    df.columns[0]: "ID_Loja",
    df.columns[1]: "Área da loja",
    df.columns[2]: "Produtos Disponíveis",
    df.columns[3]: "Visitantes",
    df.columns[4]: "Vendas da Loja",
})



# Selecionar as colunas de interesse
colunas_interesse = ["Produtos Disponíveis", "Visitantes", "Vendas da Loja"]
df_interesse = df[colunas_interesse]

# Calcular as estatísticas descritivas
estatisticas = df_interesse.agg(["min", "max", "std", "mean"])

# Exibir as estatísticas
print(estatisticas)

# ENCONTRAR OS VALORES MÍNIMO, MÁXIMO E DESVIO PADRÃO DAS COLUNAS ITENS AVALIADOS, VISITANTES E VENDAS
dados = df[[
    "Produtos Disponíveis",
    "Visitantes",
    "Vendas da Loja"
]].describe()
min = dados.loc["min"]
max = dados.loc["max"]
media = dados.loc["mean"]
desvio_padrao = dados.loc["std"]

# Exibir as estatísticas
print(dados)