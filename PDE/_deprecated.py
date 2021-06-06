import numpy as np

from PDE._typing import *
from PDE.derivator import Derivator
from PDE import (
    utils,
    _internal
    )

class System:
    FDM_ORDER: set[int] = {2, 4}
    DERIVATIVE: set[int] = {1, 2}
    # (order, derivative) -> Coefs
    C_COEF: dict[tuple[int, int], list[float]] = {
        (2, 1): [-0.5, 0, 0.5],
        (2, 2): [1, 2, 1],
        (4, 1): [1/12, -2/3, 0, 2/3, -1/12],
        (4, 2): [-1/12, 4/3, -5/2, 4/3, -1/12]
    }
    A_COEF: dict[tuple[int, int], list[float]] = {
        (2, 1): [1.5, 2, 0.5],
        (2, 2): [-2, 5, -4, 1],
        (4, 1): [25/12, -4, 3, -4/3, 1/4],
        (4, 2): [-15/14, 77/6, -107/6, 13, -61/12]
    }

    def __init__(
            self,
            init_condition: FloatArray,
            boundary_condition: Optional[VecApply]=None,
            derive_order: int = 4,
            time_dif_order: int = 1
        ):
        pass

    @classmethod
    def create_derive(cls, order: int, derive_order: int, h: float,  space_shape: Sequence[int], dim: int=0) -> VecApply:
        if order not in cls.FDM_ORDER:
            raise ValueError(f"Order {order} not supported for derivation with FDM")

        invert_h = 1 / (h ** derive_order)        
        c = np.array(cls.C_COEF[(order, derive_order)])
        a_f = np.array(cls.A_COEF[(order, derive_order)])
        a_b = -a_f[::-1]
        c_born = len(c) // 2
        a_born = len(a_b)


        def _derive(v: FloatArray) -> FloatArray:
            res = np.zeros(v.shape)
            # Centered
            for index, k in enumerate(range(-c_born, c_born + 1)):
                res = res + c[index] * np.roll(v, k, axis=dim)
            
            # forward/backward
            for f, b in utils.close_range(a_born): 
                res[(slice(None),) * dim if dim else None, f, ...] = np.sum(a_f * np.take(v, np.arange(f, f + a_born), axis=dim))
                res[(slice(None),) * dim if dim else None, b, ...] = np.sum(a_b * np.take(v, np.arange(b - a_born + 1, b + 1), axis=dim))
            
            res = res * invert_h
            return res
        
        
        return _derive