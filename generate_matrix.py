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
#     [1, 1 / sqrt(3), -1 / sqrt(3), 1 / sqrt(3)]
#     [1, -1 / sqrt(3), -1 / sqrt(3), 1 / sqrt(3)]
#     [1, 1 / sqrt(3), -1 / sqrt(3), -1 / sqrt(3)]
#     [1, -1 / sqrt(3), -1 / sqrt(3), -1 / sqrt(3)]
#     [1, 1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3)]
#     [1, -1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3)]
#     [1, 1 / sqrt(3), 1 / sqrt(3), -1 / sqrt(3)]
#     [1, -1 / sqrt(3), 1 / sqrt(3), -1 / sqrt(3)]
# ] * in (9行1列) = out(8
# 行1列)
#
#

import numpy as np


def add(x: np.ndarray, y):
    return x+y


def div(x, y):
    return x / y
