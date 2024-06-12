import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


a = 0.95
b = 0.7
c = 0.6
d = 3.5
e = 0.25
f = 0.1
dt = 0.01
num_points = 10000

x0, y0, z0 = 0.1, 0, 0


def aizawa(a, b, c, d, e, f, x0, y0, z0, dt, num_points):
    x = np.zeros(num_points)
    y = np.zeros(num_points)
    z = np.zeros(num_points)
    x[0], y[0], z[0] = x0, y0, z0
    for i in range(1, num_points):
        dx = (z[i-1] - b) * x[i-1] - d * y[i-1]
        dy = d * x[i-1] + (z[i-1] - b) * y[i-1]
        dz = c + a * z[i-1] - (z[i-1]**3 / 3) - (x[i-1]**2 + y[i-1]**2) * (1 + e * z[i-1]) + f * z[i-1] * x[i-1]**3
        x[i] = x[i-1] + dx * dt
        y[i] = y[i-1] + dy * dt
        z[i] = z[i-1] + dz * dt
    return x, y, z


x, y, z = aizawa(a, b, c, d, e, f, x0, y0, z0, dt, num_points)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim((-5, 5))
ax.set_ylim((-5, 5))
ax.set_zlim((-5, 5))
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


line, = ax.plot([], [], [], lw=0.5)


def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,


def animate(i):
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=num_points, interval=20, blit=True)

try:
    ani.save('aizawa_attractor.mp4', writer='ffmpeg', fps=30)
    print("File saved succesfully")
except Exception as e:
    print(f"Error saving animation: {e}")

plt.show()
