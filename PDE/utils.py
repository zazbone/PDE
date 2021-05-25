from PDE._typing import Generator as _Gen


def close_range(n: int, start: int=0, step: int=1) -> _Gen[tuple[int, int], None, None]:
    if step <= 0:
        raise ValueError("Negativ step not supported")
    
    head = -(start + 1)
    queu = start
    for _ in range(n // step):
        yield queu, head
        queu += step
        head -= step