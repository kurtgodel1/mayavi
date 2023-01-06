import numpy as np
from mayavi import mlab
from numpy import sin

A = 20
B = 20
limit_y = 10
limit_x = limit_y + 10
w = 1
k = 1
t = 0
divt = 10
loc = 10

x = np.linspace(-limit_x, limit_x, 200)
y = np.linspace(-limit_y, limit_y, 200)
X, Y = np.meshgrid(x, y)

# Z = sin(10*np.sqrt(X**2 + Y**2))/np.sqrt(X**2 + Y**2)


Z = A * sin(k * np.sqrt((X - loc) ** 2 + Y ** 2) - w * t) / np.sqrt((X - loc) ** 2 + Y ** 2) \
    + B * sin(k * np.sqrt((X + loc) ** 2 + Y ** 2) - w * t) / np.sqrt((X + loc) ** 2 + Y ** 2)

K = Z[Y == limit_y]
KK = np.tile(K, (y.size, 1))

# View it.
m = mlab.mesh(X, Y, KK ** 2 * 0)
s = mlab.mesh(X, Y, Z * 0)
back = mlab.mesh(X, Y, KK * 0 + limit_y, scalars=KK ** 2, colormap='black-white')

m.actor.actor.rotate_x(90)
back.actor.actor.rotate_x(90)


@mlab.animate(delay=10)
def anim():
    f = mlab.gcf()

    for tt in range(1000):
        print("Updating scene...")

        damping = np.exp(-np.sqrt(tt) / divt)
        Z = A * damping * sin(k * np.sqrt((X - loc) ** 2 + Y ** 2) - w * tt / divt) / \
            (np.sqrt((X - loc) ** 2 + Y ** 2)) \
            + B * damping * sin(k * np.sqrt((X + loc) ** 2 + Y ** 2) - w * tt / divt) / np.sqrt((X + loc) ** 2 + Y ** 2)
        Z[(np.sqrt((X - loc) ** 2 + Y ** 2) > w / k * tt / divt) & (
                    np.sqrt((X + loc) ** 2 + Y ** 2) > w / k * tt / divt)] = 0
        K = Z[Y == limit_y] ** 2
        kk = np.tile(K, (x.size, 1))
        if not tt:
            pp = kk
        else:
            pp += kk
        m.mlab_source.set(x=X, y=Y, z=kk + limit_y + 1, scalars=kk)
        s.mlab_source.set(x=X, y=Y, z=Z, scalars=Z)
        back.mlab_source.set(scalars=pp)
        yield


anim()
mlab.show()
