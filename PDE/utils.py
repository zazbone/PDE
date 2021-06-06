from typing import NamedTuple, Sequence, Optional, Any
from collections import namedtuple

from PDE.typing import Generator as _Gen


def new_argument_builder(
    name: str,
    field_names: Sequence[str],
    defaults: Optional[Any]=None,
    target_name: Optional[str]=None,
    target_purpose: Optional[str]=None,
    doc_string: Optional[str]=None
    ):
    """
    Construct FuncArg class derivated from namedtuple
    :parameter target_name: Can be function name "foo" or more detailed like "foo from module bar"
    :parameter target_purpose: Usefull if you have multiple argument builder for one function
    """
    field_names = list(field_names)
    if defaults is None:
        defaults = list()
    else:
        defaults = list(defaults)

    if target_name is None:
        doc = f"An argument constructor\n"
    else:
        doc = f"An argument constructor for funtion {target_name}\n"
    if target_purpose is None:
        doc += f"\n"
    else:
        doc += f"{target_name}\n\n"
    if doc_string is not None:
        doc += doc_string

    class FuncArg(namedtuple(name, field_names, defaults=defaults)):
        __doc__ = doc
        @classmethod
        def build(cls, *arg):
            return cls(*arg)._asdict()

    return FuncArg


def close_range(n: int, start: int=0, step: int=1) -> _Gen[tuple[int, int], None, None]:
    if step <= 0:
        raise ValueError("Negativ step not supported")
    
    head = -(start + 1)
    queu = start
    for _ in range(n // step):
        yield queu, head
        queu += step
        head -= step