from typing import NamedTuple, Sequence, Optional, Any
from collections import namedtuple


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


if __name__ == "__main__":
    def foo(x, y, z): print(x, y, z)
    FooBuilder = new_argument_builder("FooBuilder", ["x", "y", "z"], [0, 0])
    foo(**FooBuilder.build(1))
    help(FooBuilder)  # Need to make it work one day