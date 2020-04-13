import numpy as np
from math import sqrt


def convert_fuma_to_ambix_3rd_order(fuma: np.ndarray) -> np.ndarray:
    """
    :param fuma: shape = (16,)
    :return: AmbiX format. shape = (16,)
    """
    return np.multiply(
        [
            sqrt(2),  # order = 0
            1, 1, 1,  # order = 1
            sqrt(3 / 4), sqrt(3 / 4), 1, sqrt(3 / 4), sqrt(3 / 4),  # order = 2
            sqrt(5 / 8), sqrt(5 / 9), sqrt(32 / 45), 1, sqrt(32 / 45), sqrt(5 / 9), sqrt(5 / 8)  # order = 3
        ],
        fuma[[
            0,  # order = 0
            2, 3, 1,  # order = 1
            8, 6, 4, 5, 7,  # order = 2
            15, 13, 11, 9, 10, 12, 14  # order = 3
        ]])
