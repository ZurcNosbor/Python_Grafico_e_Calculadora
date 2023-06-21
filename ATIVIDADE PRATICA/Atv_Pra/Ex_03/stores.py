# IMPORT DA BIBLIOTECA PANDAS PARA MANIPULAÇÃO E ANÁLISE DE DADOS
import pandas as pd

# IMPORT PARA A GERAÇÃO DE GRAFICOS
import matplotlib.pyplot as plt

# LER O ARQUIVO "Stores.csv" NA PASTA
df = pd.read_csv("Stores.csv", sep=',', encoding='ISO 8859-1')

# RENOMEAR TODAS AS COLUNAS DO ARQUIVO
df = df.rename(columns={
    df.columns[0]: "ID_Loja",
    df.columns[1]: "Produtos",
    df.columns[2]: "Produtos Disponíveis",
    df.columns[3]: "Visitantes",
    df.columns[4]: "Vendas (DOLAR)",
})

#VER O ARQUIVO NO TERMINAL
print(df)

# SELECIONAR AS COLUNAS PARA BUSCAR OS DADOS: PRODUTOS DISPONÍVEIS, VISITANTES E VENDAS DA LOJA
col_interesse = ["Produtos Disponíveis", "Visitantes", "Vendas (DOLAR)"]
df_col_interesse = df[col_interesse]

#BUSCAR OS DADOS MÍNIMO, MÁXIMO E DESVIO PADRÃO
dados = df_col_interesse.agg(["min", "max", "std", "mean"])

#VER O ARQUIVO NO TERMINAL
print(dados)

# AMOSTRA DE 30% DOS DADOS DA COLUNA "PRODUTOS DISPONIVEIS"
amostra = df["Produtos Disponíveis"].sample(frac=0.3)

#GRÁFICO DE PRODUTOS DISPONÍVEIS
plt.scatter(amostra.index, amostra, color='blue', label='Produtos Disponíveis')

plt.xlabel('Índice')
plt.ylabel('Produtos Disponíveis')
plt.title('Análise de Produtos Disponíveis')
plt.legend()
plt.grid()
plt.show()

# AMOSTRA DE 30% DOS DADOS DA COLUNA "VISITANTES"
amostra_2 = df["Visitantes"].sample(frac=0.3)

#GRÁFICO DE PRODUTOS DISPONÍVEIS
plt.scatter(amostra_2.index, amostra_2, color='green', label='Visitantes')

plt.xlabel('Índice')
plt.ylabel('Visitantes')
plt.title('Análise de Visitantes')
plt.legend()
plt.grid()
plt.show()

# AMOSTRA DE 30% DOS DADOS DA COLUNA "Vendas (DOLAR)"
amostra_3 = df["Vendas (DOLAR)"].sample(frac=0.3)

#GRÁFICO DE PRODUTOS DISPONÍVEIS
plt.scatter(amostra_3.index, amostra_3, color='red', label='Vendas da Loja (DOLAR)')

plt.xlabel('Índice')
plt.ylabel('Vendas da Loja (DOLAR)')
plt.title('Análise de Vendas da Loja (DOLAR)')
plt.legend()
plt.grid()
plt.show()




