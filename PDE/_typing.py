from collections import abc
from collections.abc import Callable
from os import PathLike
from pathlib import PosixPath, PurePath, WindowsPath
import typing
from typing import Optional, Generator, Sequence



import numpy as np


# Miscellaneous
TypeOfPath = typing.Union[str, PosixPath, PurePath, WindowsPath, PathLike]

# Numpy data structure
FloatArray = np.ndarray
VecApply = abc.Callable[[FloatArray], FloatArray]

# Annimation
ImageArray = Sequence[FloatArray]

