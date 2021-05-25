import typing
from typing import Optional, Generator
from collections import abc
from collections.abc import Callable

import numpy as np


FloatArray = np.ndarray
VecApply = abc.Callable[[FloatArray], FloatArray]