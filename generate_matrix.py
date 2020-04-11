# Example of decoding 1st order ambisonic into 8ch cube speakers
#
# ch(1) = LFD
# ch(2) = RFD
# ch(3) = LBD
# ch(4) = RBD
# ch(5) = LFU
# ch(6) = RFU
# ch(7) = LBU
# ch(8) = RBU
#
# ch(1) = acn[0] + 0.577 * acn[1] - 0.577 * acn[2] + 0.577 * acn[3]
# ch(2) = acn[0] - 0.577 * acn[1] - 0.577 * acn[2] + 0.577 * acn[3]
# ch(3) = acn[0] + 0.577 * acn[1] - 0.577 * acn[2] - 0.577 * acn[3]
# ch(4) = acn[0] - 0.577 * acn[1] - 0.577 * acn[2] - 0.577 * acn[3]
# ch(5) = acn[0] + 0.577 * acn[1] + 0.577 * acn[2] + 0.577 * acn[3]
# ch(6) = acn[0] - 0.577 * acn[1] + 0.577 * acn[2] + 0.577 * acn[3]
# ch(7) = acn[0] + 0.577 * acn[1] + 0.577 * acn[2] - 0.577 * acn[3]
# ch(8) = acn[0] - 0.577 * acn[1] + 0.577 * acn[2] - 0.577 * acn[3]

# [
#     [1, 1/sqrt(3), -1/sqrt(3), 1/sqrt(3)],
#     [1, -1/sqrt(3), -1/sqrt(3), 1/sqrt(3)],
#     [1, 1/sqrt(3), -1/sqrt(3), -1/sqrt(3)],
#     [1, -1/sqrt(3), -1/sqrt(3), -1/sqrt(3)],
#     [1, 1/sqrt(3), 1/sqrt(3), 1/sqrt(3)],
#     [1, -1/sqrt(3), 1/sqrt(3), 1/sqrt(3)],
#     [1, 1/sqrt(3), 1/sqrt(3), -1/sqrt(3)],
#     [1, -1/sqrt(3), 1/sqrt(3), -1/sqrt(3)]
# ] * in (4行1列) = out (8行1列)
#
#

import numpy as np
from math import sqrt, sin, cos, pi, asin

Rad = float  # angles in radian


def coefs(az: Rad, el: Rad, order: int = 1) -> np.ndarray:
    """
    :param az: azimuth
    :param el: elevation
    :param order: ambisonic order
    :return: 1 dimensional ndarray
    """
    return np.array([
        1,  # acn[0], W
        sin(az) * cos(el),  # acn[1], Y
        sin(el),  # acn[2], Z
        cos(az) * cos(el),  # acn[3], X
        sqrt(3) / 2 * sin(2 * az) * (cos(el) ** 2),  # acn[4], V
        sqrt(3) / 2 * sin(az) * sin(2 * el),  # acn[5], T
        1 / 2 * (3 * (sin(el) ** 2) - 1),  # acn[6], R
        sqrt(3) / 2 * cos(az) * sin(2 * el),  # acn[7], S
        sqrt(3) / 2 * cos(2 * az) * cos(el) ** 2,  # acn[8], U
    ])[0:(order + 1) ** 2]


def matrix_for_cube_decode(order: int = 1) -> np.ndarray:
    def get_coefs(az: Rad, el: Rad):
        return coefs(az, el, order)

    return np.array([
        get_coefs(1 / 4 * pi, -asin(1 / sqrt(3))),
        get_coefs(7 / 4 * pi, -asin(1 / sqrt(3))),
        get_coefs(3 / 4 * pi, -asin(1 / sqrt(3))),
        get_coefs(5 / 4 * pi, -asin(1 / sqrt(3))),
        get_coefs(1 / 4 * pi, asin(1 / sqrt(3))),
        get_coefs(7 / 4 * pi, asin(1 / sqrt(3))),
        get_coefs(3 / 4 * pi, asin(1 / sqrt(3))),
        get_coefs(5 / 4 * pi, asin(1 / sqrt(3))),
    ])


def decode(input_matrix: np.ndarray, order: int = 1) -> np.ndarray:
    return np.dot(matrix_for_cube_decode(order), input_matrix)
