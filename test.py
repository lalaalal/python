# by 협창쓰
# date 2019.05.05

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

X_REAL = np.arange(-5, 5, 0.1)
X_IMAG = np.arange(-5, 5, 0.1)

X_REAL, X_IMAG = np.meshgrid(X_REAL, X_IMAG)

i = 0
Y_REAL = []
Y_IMAG = []
while i < len(X_REAL):
    j = 0
    while j < len(X_REAL[0]):
        tmp = complex(X_REAL[i][j], X_IMAG[i][j]) ** 2
        Y_REAL.append(tmp.real)
        Y_IMAG.append(tmp.imag)
        j += 1
    i += 1

Y_REAL = np.asarray(Y_REAL).reshape((len(X_REAL), len(X_REAL[0])))
Y_IMAG = np.asarray(Y_IMAG).reshape((len(X_REAL), len(X_REAL[0])))

minn, maxx = Y_IMAG.min(), Y_IMAG.max()

norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
fcolors = m.to_rgba(Y_IMAG)
m.set_array(Y_IMAG)
fig.colorbar(m).set_label("Y-IMAG")

surf = ax.plot_surface(X_REAL, Y_REAL, X_IMAG, facecolors=fcolors,
                       vmin=minn, vmax=maxx, shade=False, linewidth=0)
ax.set_xlabel("X-REAL")
ax.set_ylabel("Y-REAL")
ax.set_zlabel("X-IMAG")

plt.show()
