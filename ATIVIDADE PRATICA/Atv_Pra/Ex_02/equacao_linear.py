#IMPORT PARA A GERAÇÃO DE GRAFICOS
import matplotlib.pyplot as plt

#MEU RU - COMO PEDE NO ENUNCIADO, UTILIZEI OS 3 PRIMEIROS DIGITOS
RU = 3773638
a = 3
b = 7
c = 7

#CRIAÇÃO DO VETOR COM 10 POSIÇOES
vetorX = list(range(1, 11))

#CALCULA OS VALORES DE Y COM A EQUAÇÃO PARA VALOR DE X NO VETOR
y = [a * vetorXi + b * vetorXi - c for vetorXi in vetorX]

#PLOTAR OS PONTOS COM CORES
plt.plot(vetorX[0], y[0], marker = "o", markersize=12, markerfacecolor='blue')
plt.plot(vetorX[1], y[1], marker = "o", markersize=12, markerfacecolor='red')
plt.plot(vetorX[2], y[2], marker = "o", markersize=12, markerfacecolor='green')
plt.plot(vetorX[3], y[3], marker = "o", markersize=12, markerfacecolor='black')
plt.plot(vetorX[4], y[4], marker = "o", markersize=12, markerfacecolor='yellow')
plt.plot(vetorX[5], y[5], marker = "o", markersize=12, markerfacecolor='orange')
plt.plot(vetorX[6], y[6], marker = "o", markersize=12, markerfacecolor='brown')
plt.plot(vetorX[7], y[7], marker = "o", markersize=12, markerfacecolor='pink')
plt.plot(vetorX[8], y[8], marker = "o", markersize=12, markerfacecolor='silver')
plt.plot(vetorX[9], y[9], marker = "o", markersize=12, markerfacecolor='purple')

# NOMEAR EIXO X
plt.xlabel('EIXO X')

# NOMEAR EIXO Y
plt.ylabel('EIXO Y')

#LEGENDA DO GRÁFICO
plt.legend([f'POSIÇÃO X={vetorX[0]} POSIÇÃO Y={y[0]}',
            f'POSIÇÃO X={vetorX[1]} POSIÇÃO Y={y[1]}',
            f'POSIÇÃO X={vetorX[2]} POSIÇÃO Y={y[2]}',
            f'POSIÇÃO X={vetorX[3]} POSIÇÃO Y={y[3]}',
            f'POSIÇÃO X={vetorX[4]} POSIÇÃO Y={y[4]}',
            f'POSIÇÃO X={vetorX[5]} POSIÇÃO Y={y[5]}',
            f'POSIÇÃO X={vetorX[6]} POSIÇÃO Y={y[6]}',
            f'POSIÇÃO X={vetorX[7]} POSIÇÃO Y={y[7]}',
            f'POSIÇÃO X={vetorX[8]} POSIÇÃO Y={y[8]}',
            f'POSIÇÃO X={vetorX[9]} POSIÇÃO Y={y[9]}'])

#GRADE NO GRÁFICO
plt.grid()

# TÍTULO DO GRÁFICO
plt.title('Exercício 02 - EQUAÇÃO LINEAR')

# MOSTRAR GRÁFICO
plt.show()
