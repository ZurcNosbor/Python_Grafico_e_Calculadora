# IMPORT PARA A GERAÇÃO DE GRAFICOS
import matplotlib.pyplot as plt

# IMPORT DO RANDOM PARA GERAR NUMEROS ALEATORIOS
import random

# MEU RU - COMO PEDE NO ENUNCIADO, UTILIZEI OS 3 PRIMEIROS DIGITOS
RU = 3773638
a = 3
b = 7
c = 7

# GERA VETOR COM 10 POSIÇÕES COM NÚMEROS ALEÁTORIOS DO NÚMERO 1 AO 25 COMO EXEMPLO
vetorX = random.sample(range(1, 25), 10)

# CALCULA OS VALORES DE Y COM A EQUAÇÃO PARA VALOR DE X NO VETOR
y = [a * vetorXi + b * vetorXi - c for vetorXi in vetorX]

# ORDENA OS PONTOS EM ORDEM CRESCENTE COM BASE NO VETOR
pontos_ordenados = sorted(zip(vetorX, y))

vetorX_ordenado, y_ordenado = zip(*pontos_ordenados)

# PLOTAR OS PONTOS COM CORES
for i in range(len(vetorX_ordenado)):
    plt.plot(vetorX_ordenado[i], y_ordenado[i], marker="o", markersize=12)

# NOMEAR EIXO X
plt.xlabel('EIXO X')

# NOMEAR EIXO Y
plt.ylabel('EIXO Y')

# LEGENDA DO GRÁFICO
legend_labels = [f'POSIÇÃO X={vetorX_ordenado[i]} POSIÇÃO Y={y_ordenado[i]}' for i in range(len(vetorX_ordenado))]
plt.legend(legend_labels)

# GRADE NO GRÁFICO
plt.grid()

# TÍTULO DO GRÁFICO
plt.title('Exercício 02 - EQUAÇÃO LINEAR')

# MOSTRAR GRÁFICO
plt.show()
