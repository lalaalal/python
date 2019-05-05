from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')

x = []
y = []

i_min = -5
while i_min <= 5:
    r_min = -5
    while r_min <= 5:
        tmp = complex(r_min, i_min)
        x.append(tmp)
        y.append(tmp ** 2)
        r_min += 0.1
    i_min += 0.1

x_r = []
x_i = []
y_r = []
y_i = []

for i in x:
    x_r.append(i.real)
    x_i.append(i.imag)

for j in y:
    y_r.append(j.real)
    y_i.append(j.imag)

colormap = y_i
ax.scatter(x_r, y_r, x_i, s=50, c=colormap)
plt.show()
