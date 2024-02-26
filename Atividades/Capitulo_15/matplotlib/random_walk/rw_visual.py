import matplotlib.pyplot as plt
from random import choice
from random_walk import RandomWalk


while True:
    # Cria um random walk
    # escolha = choice(plt.style.available)
    plt.style.use('dark_background')
    # print(f'escolha: {escolha}')

    rw = RandomWalk(50_000)
    rw.fill_walk()

    # plota os pontos no passeio e set ao tamanho da figura que será mostrada
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)

    # simulação de um caminho aleatório de um grão de pólen na superfície de uma gota de água
    # ax.plot(rw.x_values, rw.y_values, linewidth=1)
    # ax.plot(0, 0, linewidth=1)
    # ax.plot(rw.x_values[-1], rw.y_values[-1], linewidth=1)

    ax.scatter(rw.x_values, rw.y_values, s=1 , c=point_numbers, cmap=plt.cm.Reds, edgecolors='none')
    ax.scatter(0, 0, s=50 , c='green', cmap=plt.cm.Blues, edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], s=50 , c='red', cmap=plt.cm.Blues, edgecolors='none')
    ax.set_aspect('equal')

    # Remove os eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
