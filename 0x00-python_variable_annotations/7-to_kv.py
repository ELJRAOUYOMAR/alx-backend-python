#!/usr/bin/env python3
""" docs """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Func doc"""
    return (k, v**2)
