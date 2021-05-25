from PDE import System
import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import approx_fprime

stop = 10
step = 100

deriv = System.create_derive(order=4, derive_order=1, h=stop / step)
t = np.linspace(0, stop, step)

plt.plot(t, np.sin(t))
plt.plot(t, deriv(np.cos(t)))
plt.show()