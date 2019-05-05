import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


a = float(input())

def xrange(min, max, interval):
    numbers = []
    while min < max:
        numbers.append(min)
        min += interval
    return numbers


fig = plt.figure(figsize=(5, 5))
ax = fig.gca(projection='3d')

x = xrange(-3, 3, 0.01)
y = []
for t in x:
    y.append(((a) ** t).real)

z = []
for t in x:
    z.append(((a) ** t).imag)

ax.plot(x, y, z, linewidth=1)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Y-imag")
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
plt.title(label="y = (%.2f)^x" % a)
plt.show()

# plt.figure(figsize=(10, 7))
#
# plt.subplot(121)
# x = xrange(-3, 3, 0.005)
# y = []
# for i in x:
#     y.append(0)
#
# plt.scatter(x, y, s=50, c=x)
#
# plt.subplot(122)
# y = []
# for t in x:
#     y.append(((-1.5) ** t).real)
#
# z = []
# for t in x:
#     z.append(((-1.5) ** t).imag)
#
# plt.scatter(y, z, s=50, c=x)
# plt.show()
