import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def julia_set(width, height, x_min, x_max, y_min, y_max, c_real, c_imag, max_iter):
    x_vals = np.linspace(x_min, x_max, width)
    y_vals = np.linspace(y_min, y_max, height)
    julia = np.zeros((width, height))
    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            z = complex(x, y)
            for k in range(max_iter):
                z = z**2 + complex(c_real, c_imag)
                if abs(z) > 2:
                    julia[i, j] = k
                    break
    return julia


xmin, xmax, ymin, ymax = -2, 2, -2, 2
width, height = 1000, 1000
c_real, c_imag = -0.7, 0.27015
max_iter = 100

frames = []
for i in range(max_iter):
    julia = julia_set(width, height, xmin, xmax, ymin, ymax, c_real, c_imag, i)
    frames.append(julia)

def update(frame):
    ax.clear()
    ax.imshow(frames[frame], extent=(xmin, xmax, ymin, ymax), cmap='inferno', interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Iteration: {frame}")
    return ax

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=100)
ani.save('JuliaSet.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
plt.show()
