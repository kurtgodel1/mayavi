import numpy as np
from matplotlib import pyplot as plt
from mayavi import mlab

"""
x1,x2 = (-.199995,-.19999)
y1,y2 = (-1.10024,-1.10025)
"""
plt.cla()
x1, x2 = (0.3694, 0.3697)
y2, y1 = (0.109, 0.1094)

x = np.linspace(x1, x2, 2000)
y = np.linspace(y1, y2, 2000)

X, Y = np.meshgrid(x, y)

C = X + 1j * Y
M = np.zeros(np.shape(X), dtype=int)
Z = np.zeros(np.shape(X), dtype=complex)

# M[np.absolute(C) < 2] +=1
# C[abs(C)<2] = C[abs(C)<2]**2
for i in range(200):
    K = abs(Z)
    M[K < 2] += 1
    Z[K < 2] = Z[K < 2] ** 2 + C[K < 2]

# M[M==M.max()] = 1
plt.imshow(M, extent=(x1, x2, y2, y1))
plt.show()

fig = mlab.figure(1)

mesh = mlab.imshow(-M / M.max() * (x2 - x1), colormap='YlOrBr')

mlab.show()
