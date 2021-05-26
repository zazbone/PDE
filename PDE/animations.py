from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from PDE import (
    MODULE_PATH,
    _typing as _ty
    )


def anim1D(x: _ty.FloatArray, images_array: _ty.ImageArray, dt: float, output_name: _ty.TypeOfPath):
    output_name = Path(output_name)
    fig = plt.figure(figsize=(15, 15))
    def animate(i):
        plt.clf()
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.plot(x, images_array[i], color='b')

    ani = FuncAnimation(fig, animate, interval=dt * 1000)
    ani.save(output_name.with_suffix(".mp4"))


    