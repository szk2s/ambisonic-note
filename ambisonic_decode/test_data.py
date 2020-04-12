from typing import List
from .type_definitions import TestData
import numpy as np


data_of_1st_order: List[TestData] = [
    TestData(np.array([[1, 0, 0, 0]]).T, np.array([[1, 1, 1, 1, 1, 1, 1, 1]]).T, 1),
    TestData(np.array([[0, 1, 0, 0]]).T,
             np.array(
                 [[0.57735027, -0.57735027, 0.57735027, -0.57735027, 0.57735027, -0.57735027, 0.57735027,
                   -0.57735027]]).T,
             1),
    TestData(np.array([[0, 0, 1, 0]]).T,
             np.array(
                 [[-0.57735027, -0.57735027, -0.57735027, -0.57735027, 0.57735027, 0.57735027, 0.57735027,
                   0.57735027]]).T,
             1),
    TestData(np.array([[0, 0, 0, 1]]).T,
             np.array([[0.57735027, 0.57735027, -0.57735027, -0.57735027, 0.57735027, 0.57735027, -0.57735027,
                        -0.57735027]]).T,
             1)
]

data_of_2nd_order: List[TestData] = [
    TestData(np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0]]).T,
             np.array([[1, 1, 1, 1, 1, 1, 1, 1]]).T,
             2)
]

data_of_3rd_order: List[TestData] = [
    TestData(np.array([[1, 0, 0, 0, 0,
                        0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0,
                        0]]).T,
             np.array([[1, 1, 1, 1, 1, 1, 1, 1]]).T,
             3)
]

data_for_decode_test = data_of_1st_order + data_of_2nd_order + data_of_3rd_order


