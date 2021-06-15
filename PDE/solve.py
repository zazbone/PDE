import numpy as np

from PDE.typing import FloatArray

def thomas(A: FloatArray, x: FloatArray, d: FloatArray) -> FloatArray:
    a = np.diag(A, k=-1)
    a = np.append(a, a[0])
    b = np.diag(A).copy()
    c = np.diag(A, k=1)
    c = np.append(c, c[0])
    x = x.copy()
    d = d.copy()
    n = len(x)
    for i in range(1, n):
        w = a[i] / b[i - 1]
        b[i] = b[i] - w * c[i - 1]
        d[i] = d[i] - w * d[i - 1]
    
    x[-1] = d[-1] / d[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]
    
    return x