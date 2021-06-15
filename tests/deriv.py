from PDE import Derivator, animations, MODULE_PATH
import numpy as np
import matplotlib.pyplot as plt


stop = 10
step = 100

t = np.linspace(1, stop, step)
deriv = Derivator(t.shape, 1, 4, 0.1, lambda x: x)

plt.plot(t,  t / t, 'r')
plt.plot(t, deriv.D(1, 0, t), 'b')
plt.show()


delat_t = 0.1
delta_x = 0.05
x_max = 10
t_max = 10
c = 0.3

def b(u):
    u[0] = 2
    u[-1] = 2
    return u

x = np.arange(0, x_max, delta_x)
u = np.sin(x) + 2
derive2 = Derivator(x.shape, 2, 2, delta_x, b)
image_array = [u]
for _ in np.arange(0, t_max, delat_t):
    u = u + delat_t * c *  derive2.D(1,0,u)
    image_array.append(u)

animations.anim1D(x, image_array, delat_t, MODULE_PATH.parent / "tests/out.mp4")

