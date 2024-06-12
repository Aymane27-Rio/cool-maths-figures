import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

def update(frame):
    ax.clear()
    ax.imshow(frames[frame], extent=(xmin, xmax, ymin, ymax))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Iterations: {frame}")
    return ax


xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 100


frames = []
for i in range(max_iter):
    frames.append(mandelbrot_set(xmin, xmax, ymin, ymax, width, height, i)[2])


fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=100)
ani.save('mandelbrot.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
plt.show()
