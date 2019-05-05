from matplotlib import pyplot as plt


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Quardratic Function Graph')


def xrange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start += interval
    return numbers


def make_x_y(xmin, xmax):
    x = xrange(xmin, xmax, 0.001)
    y = []
    for t in x:
        y.append(2 ** t)
    draw_graph(x, y)


make_x_y(-1, 3)
plt.show()
