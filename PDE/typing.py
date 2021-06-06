from collections.abc import Callable
from os import PathLike
from pathlib import PosixPath, PurePath, WindowsPath
from typing import Optional, Generator, Sequence, Union

import numpy as np


# Miscellaneous
TypeOfPath = Union[str, PosixPath, PurePath, WindowsPath, PathLike]

# Numpy data structure
FloatArray = np.ndarray
VecApply = Callable[[FloatArray], FloatArray]

# Annimation
ImageArray = Sequence[FloatArray]
