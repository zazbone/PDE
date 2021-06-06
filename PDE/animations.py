from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from PDE import (
    MODULE_PATH,
    )
from PDE.typing import FloatArray, ImageArray, TypeOfPath


def anim1D(x: FloatArray, images_array: ImageArray, dt: float, output_name: TypeOfPath):
    output_name = Path(output_name)
    fig = plt.figure(figsize=(15, 15))
    def animate(i):
        plt.clf()
        plt.xlim(-1, 10)
        plt.ylim(-1, 10)
        plt.plot(x, images_array[i], color='b')

    ani = FuncAnimation(fig, animate, interval=dt * 1000)
    ani.save(output_name.with_suffix(".mp4"))


    