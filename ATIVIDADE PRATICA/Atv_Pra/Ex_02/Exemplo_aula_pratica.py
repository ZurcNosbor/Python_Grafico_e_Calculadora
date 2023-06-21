from matplotlib import pyplot as plt
# o menu ira resultar nos valores de y1, y2 e y3 por meio da equação ax + bx - c
def menu(x, a, b, c):
    y = a*x + b*x - c
    return y

# definindo os valores para x:
x1 = 5
x2 = 7
x3 = 9

#definindo os valores para a, b e c:
a = 3
b = 7
c = 7

#colocando titulo e folha quadriculada no grafico:
plt.title('equação do exercicio')
plt.grid()

# plotando os resultados obtidos por x e y:
plt.plot(x1, menu(x1, a, b, c), marker = "o", markersize=15, markerfacecolor='blue')
plt.plot(x2, menu(x2, a, b, c), marker = "o", markersize=15, markerfacecolor='red')
plt.plot(x3, menu(x3, a, b, c), marker = "o", markersize=15, markerfacecolor='green')

#colocando legnda no gráfico
plt.legend([f'x={x1} y={menu(x1, a, b, c)}', f'x={x2} y={menu(x2, a, b, c)}', f'x={x3} y={menu(x3, a, b, c)}'])

plt.show()