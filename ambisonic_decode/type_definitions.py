from typing import NamedTuple
import numpy as np

Rad = float  # angles in radian


class TestData(NamedTuple):
    input: np.ndarray
    decoded: np.ndarray
    order: int = 1

