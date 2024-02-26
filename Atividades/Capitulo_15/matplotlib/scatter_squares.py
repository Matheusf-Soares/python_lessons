import matplotlib.pyplot as plt

x_values = [x for x in range(1, 1001)]
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10, color=(0.8, 0, 0.8)) # color define uma cor para os pontos usando um padrão rgb, é possível passar o nome da corr também
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

# Define o título do gráfico e os eixos do rótulo
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Define o intervalo para cada eixo
ax.axis([0, 1100] + [0, 1_100_000])
# Ordena à Matplotlib que use a notação simples para exibição de números
ax.ticklabel_format(style='plain')

# Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

plt.show()