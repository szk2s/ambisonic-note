import numpy as np
import pytest
from .generate_matrix import matrix_for_cube_decode, coefs, decode
from math import pi
from random import random
from typing import List, NamedTuple
from .type_definitions import Rad


class TestData(NamedTuple):
    input: np.ndarray
    decoded: np.ndarray
    order: int = 1


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

all_test_data = data_of_1st_order + data_of_2nd_order + data_of_3rd_order


def random_az() -> Rad:
    return random() * 2 * pi


def random_el() -> Rad:
    return (random() - 0.5) * pi


@pytest.mark.parametrize("order", [0, 1, 2, 3])
class TestCoefs(object):

    def test_is_ndarray(self, order: int) -> None:
        assert type(coefs(random_az(), random_el(), order)) == np.ndarray

    def test_shape(self, order: int) -> None:
        assert coefs(random_az(), random_el(), order).shape == ((order + 1) ** 2,)

    def test_range(self, order: int) -> None:
        result = coefs(random_az(), random_el(), order)
        ones = np.ones(result.shape)
        assert np.all(np.greater_equal(result, ones * -1))
        assert np.all(np.less_equal(result, ones))


class TestMatrixForCubeDecode(object):

    def test_decode_1st_order(self) -> None:
        mat = matrix_for_cube_decode(order=1)
        assert type(mat) == np.ndarray
        assert mat.shape == (8, 4)

    def test_decode_2nd_order(self) -> None:
        mat = matrix_for_cube_decode(order=2)
        assert type(mat) == np.ndarray
        assert mat.shape == (8, 9)

    def test_decode_3rd_order(self) -> None:
        mat = matrix_for_cube_decode(order=3)
        assert type(mat) == np.ndarray
        assert mat.shape == (8, 16)


class TestDecode(object):

    @pytest.mark.parametrize("test_data", all_test_data)  # type: ignore
    def test_decode(self, test_data: TestData) -> None:
        order = test_data.order
        assert test_data.input.shape == ((order + 1) ** 2, 1)
        result = decode(test_data.input, test_data.order)
        assert type(result) == np.ndarray
        assert result.shape == (8, 1)
        assert test_data.decoded.shape == (8, 1)
        np.testing.assert_array_almost_equal(result, test_data.decoded)
