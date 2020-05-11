from typing import Union, TypeVar, Any
from sqlalchemy import Column


T = TypeVar('T')


def eq(col, val):  # type: (Column[T], T)->Any
    return col == val
