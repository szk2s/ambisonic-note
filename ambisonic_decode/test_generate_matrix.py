import numpy as np
import pytest
from .generate_matrix import matrix_for_cube_decode, coefs, decode
from math import pi
from random import random
from typing import List, NamedTuple
from .type_definitions import Rad


class TestData(NamedTuple):
    test_input: np.ndarray
    expected: np.ndarray
    order: int = 1


data_of_first_order: List[TestData] = [
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

    def test_is_ndarray(self) -> None:
        assert type(matrix_for_cube_decode()) == np.ndarray

    def test_shape(self) -> None:
        assert matrix_for_cube_decode(order=1).shape == (8, 4)

    @pytest.mark.parametrize("input_matrix,expected", data_of_first_order)
    def test_decode_1st_order(self, input_matrix: np.ndarray, expected: np.ndarray) -> None:
        assert input_matrix.shape == (4, 1)
        mat = matrix_for_cube_decode(order=1)
        decoded = np.dot(mat, input_matrix)
        assert decoded.shape == (8, 1)
        assert expected.shape == (8, 1)
        np.testing.assert_array_almost_equal(decoded, expected)

    @pytest.mark.parametrize("input_matrix,expected", data_of_first_order)
    def test_decode_2nd_order(self, input_matrix: np.ndarray, expected: np.ndarray) -> None:
        assert input_matrix.shape == (4, 1)
        mat = matrix_for_cube_decode(order=2)
        decoded = np.dot(mat, np.array([[
            1, 1, 1, 1, 1,
            1, 1, 1, 1
        ]]).T)
        assert decoded.shape == (8, 1)

    @pytest.mark.parametrize("input_matrix,expected", data_of_first_order)
    def test_decode_3rd_order(self, input_matrix: np.ndarray, expected: np.ndarray) -> None:
        assert input_matrix.shape == (4, 1)
        mat = matrix_for_cube_decode(order=3)
        decoded = np.dot(mat, np.array([[
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1
        ]]).T)
        assert decoded.shape == (8, 1)


class TestDecode(object):

    @pytest.mark.parametrize("input_matrix,expected", data_of_first_order)
    def test_decode(self, input_matrix, expected) -> None:
        result = decode(input_matrix, 1)
        assert type(result) == np.ndarray
        assert result.shape == (8, 1)
        np.testing.assert_array_almost_equal(result, expected)
