from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from PDE import (
    MODULE_PATH,
    )
from PDE.typing import FloatArray, ImageArray, TypeOfPath


def anim1D(x: FloatArray, images_array: ImageArray, dt: float, lim: list[int]):
    fig, ax = plt.subplots()
    ax.set_xlim(lim[0:2])
    ax.set_ylim(lim[2:])
    line, = ax.plot([], [], color='b', lw=2)
    def animate(i):
        line.set_data(x, images_array[i])
        return (line,)

    return FuncAnimation(fig, animate, interval=dt * 1000)


    