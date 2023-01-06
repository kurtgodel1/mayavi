import numpy as np
from mayavi import mlab
from scipy.special import sph_harm

# Create a sphere
r = .1
pi = np.pi
cos = np.cos
sin = np.sin

# not conventianal theta and phi
phi, theta = np.mgrid[0:pi:101j, 0:2 * pi:101j]

# |m| <= n.
m = 2
n = 3
ind = 40
z_offset = 10 * r

s = sph_harm(m, n, theta, phi).real

mlab.mesh(theta * r, phi * r, (s - z_offset), scalars=s, opacity=.3)

mlab.plot3d(theta[phi == phi[ind, 0]] * r,
            phi[phi == phi[ind, 0]] * r,
            s[phi == phi[ind, 0]] - z_offset,
            line_width=r / 10, tube_radius=r / 10)

point = mlab.points3d(theta[phi == phi[ind, 0]][0] * r,
                      phi[phi == phi[ind, 0]][0] * r,
                      s[phi == phi[ind, 0]][0] - z_offset,
                      scale_factor=.05, color=(1, 0, 0))

x = r * sin(phi) * cos(theta)
y = r * sin(phi) * sin(theta)
z = r * cos(phi)

xs = s * sin(phi) * cos(theta)
ys = s * sin(phi) * sin(theta)
zs = s * cos(phi)

harmonic_points_x = x + xs
harmonic_points_y = y + ys
harmonic_points_z = z + zs

mlab.mesh(x,
          y,
          z,
          scalars=s * 0, colormap='jet', opacity=.3)

mlab.mesh(harmonic_points_x,
          harmonic_points_y,
          harmonic_points_z,
          scalars=s, colormap='jet', opacity=.3)

q = mlab.quiver3d(0, 0, 0, harmonic_points_x[phi == phi[ind, 0]][0],
                  harmonic_points_y[phi == phi[ind, 0]][0],
                  harmonic_points_z[phi == phi[ind, 0]][0],
                  mode="arrow", line_width=0.1, scale_factor=1)

func = mlab.plot3d(harmonic_points_x[phi == phi[ind, 0]],
                   harmonic_points_y[phi == phi[ind, 0]],
                   harmonic_points_z[phi == phi[ind, 0]],
                   line_width=r / 10, tube_radius=r / 10)


@mlab.animate(delay=100)
def anim():
    for jj in range(100):
        for ii in range(len(harmonic_points_x[phi == phi[ind, 0]])):
            point.mlab_source.set(x = theta[phi == phi[ind, 0]][ii] * r,
                                  y = phi[phi == phi[ind, 0]][ii] * r,
                                  z = s[phi == phi[ind, 0]][ii] - z_offset)
            q.mlab_source.set(u=harmonic_points_x[phi == phi[ind, 0]][ii],
                              v=harmonic_points_y[phi == phi[ind, 0]][ii],
                              w=harmonic_points_z[phi == phi[ind, 0]][ii])
            yield

anim()
mlab.show()
"""

x = (r) * sin(phi) * cos(theta)
y = (r) * sin(phi) * sin(theta)
z = (r) * cos(phi)
mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
mlab.clf()
# Represent spherical harmonics on the surface of the sphere
for n in range(1, 6):
    for m in range(n):
        s = sph_harm(m, n, theta, phi).real

        mlab.mesh(x - m, y - n, z, scalars=s, colormap='jet')

        s[s < 0] *= 0.97

        s /= s.max()
        mlab.mesh(s * x - m, s * y - n, s * z + 1.3,
                  scalars=s, colormap='Spectral')
mlab.view(90, 70, 6.2, (-1.3, -2.9, 0.25))

mlab.show()
"""