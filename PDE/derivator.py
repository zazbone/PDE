from typing import Tuple, Union, Sequence, Optional
from collections.abc import Iterable

import numpy as np

from PDE.typing import FloatArray, VecApply


class Derivator:
    FDM_ORDER: set[int] = {2, 4}
    MAX_DERIVATIV_ORDER: int = 2
    MAX_SYSTEM_DIM: int = 2
    # (order, derivative) -> Coefs
    C_COEF: dict[tuple[int, int], list[float]] = {
        (2, 1): [-0.5, 0, 0.5],
        (2, 2): [1, 2, 1],
        (4, 1): [1/12, -2/3, 0, 2/3, -1/12],
        (4, 2): [-1/12, 4/3, -5/2, 4/3, -1/12]
    }
    A_COEF: dict[tuple[int, int], list[float]] = {
        (2, 1): [-1.5, 2, -0.5],
        (2, 2): [2, -5, 4, -1],
        (4, 1): [-25/12, 4, -3, 4/3, -1/4],
        (4, 2): [15/14, -77/6, 107/6, -13, 61/12]
    }

    def __init__(
        self,
        system_shape: Tuple[int],
        derive_order: int,
        FDM_order: int,
        space_interval: Union[Sequence[float], float],
        boundary_condition: Optional[VecApply]
        ):
        if derive_order > type(self).MAX_DERIVATIV_ORDER:
            raise ValueError(f"Derive order should not exces {MAX_DERIVATIV_ORDER}")
        if FDM_order not in type(self).FDM_ORDER:
            raise ValueError(f"Derivation methode order not supported")
        self._dim = system_shape
        self.FDM_order = FDM_order
        if isinstance(space_interval, Iterable):
            self._inverth = [1 / h for h in list(space_interval)]
        else:
            self._inverth = [1 / space_interval] * len(self._dim)
        self._deriv = {i: list() for i in range(1, derive_order + 1)}
        self._bound = boundary_condition
        for key in self._deriv:
            for i in range(1, len(self._dim) + 1):
                self._deriv[key].append(self.create_derive(key, i))

    def create_derive(self, dorder: int, axis: int) -> VecApply:
        c = np.array(type(self).C_COEF[(self.FDM_order, dorder)])
        a_f = np.array(type(self).A_COEF[(self.FDM_order, dorder)])
        a_b = -a_f[::-1]
        clim = len(c) // 2
        alim = len(a_f)
        doc= f"""
        Centered finite differences methode
        {dorder} order derivative vectorized over {axis + 1}th dimension

        centered coeficient: {c}
        forward coeficient: {a_f}
        backward coreficient: -forward_coeficient\
        """
        if len(self._dim) == 1:
            M = np.zeros((self._dim[0], self._dim[0]))
            for row in range(len(M)):
                if row <= clim:
                    M[row, row:(alim + row)] =a_f
                elif row >= self._dim[0] - clim:
                    M[row, (row - alim + 1):(row + 1)] = a_b
                else:
                    M[row, (row - clim):(row + clim + 1)] = c

            def derive(u: FloatArray) -> FloatArray:
                bounded = self._bound(u)
                return M.dot(bounded) * self._inverth[axis - 1]
            derive.__doc__ = doc
            return derive
        
    def D(self, order: int, axis: int, u: FloatArray) -> FloatArray:
        return self._deriv[order][axis](u)

