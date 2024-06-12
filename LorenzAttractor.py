import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


sigma = 10
rho = 28
beta = 8 / 3
dt = 0.01
num_points = 1000

x0, y0, z0 = 1, 1, 1


def lorenz(sigma, rho, beta, x0, y0, z0, dt, num_points):
    x, y, z = np.zeros(num_points), np.zeros(num_points), np.zeros(num_points)
    x[0], y[0], z[0] = x0, y0, z0
    for i in range(1, num_points):
        x[i] = x[i-1] + sigma * (y[i-1] - x[i-1]) * dt
        y[i] = y[i-1] + (x[i-1] * (rho - z[i-1]) - y[i-1]) * dt
        z[i] = z[i-1] + (x[i-1] * y[i-1] - beta * z[i-1]) * dt
    return x, y, z


x, y, z = lorenz(sigma, rho, beta, x0, y0, z0, dt, num_points)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim((-20, 20))
ax.set_ylim((-30, 30))
ax.set_zlim((0, 50))
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
    ani.save('LorenzAttractor.mp4', writer='ffmpeg', fps=30)
    print("File has been saved succesfully")
except Exception as e:
    print(f"Error saving animation: {e}")

plt.show()
