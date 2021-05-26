from PDE import System, animations, MODULE_PATH
import numpy as np
import matplotlib.pyplot as plt


stop = 10
step = 100

deriv = System.create_derive(order=4, derive_order=1, h=stop / step)
t = np.linspace(0, stop, step)

plt.plot(t, np.cos(t), 'r')
plt.plot(t, deriv(np.sin(t)), 'b')
plt.show()


delat_t = 0.1
delta_x = 0.1
x_max = 10
t_max = 10
c = 0.3
derive2 = System.create_derive(4, 1, delta_x)
x = np.arange(0, x_max, delta_x)
u = np.sin(x) + 2
image_array = [u]
for _ in np.arange(0, t_max, delat_t):
    print(derive2(u)[0])
    u = u + delat_t * c * derive2(u)
    image_array.append(u)

animations.anim1D(x, image_array, delat_t, MODULE_PATH.parent / "tests/test1.mp4")
