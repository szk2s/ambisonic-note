import numpy as np
import pytest
from generate_matrix import matrix_for_cube_decode, coefs, decode
from math import pi, asin, sqrt
from random import random

fixtures = [
    (np.array([[1, 0, 0, 0]]).T, np.array([[1, 1, 1, 1, 1, 1, 1, 1]]).T),
    (np.array([[0, 1, 0, 0]]).T,
     np.array(
         [[0.57735027, -0.57735027, 0.57735027, -0.57735027, 0.57735027, -0.57735027, 0.57735027, -0.57735027]]).T),
    (np.array([[0, 0, 1, 0]]).T,
     np.array(
         [[-0.57735027, -0.57735027, -0.57735027, -0.57735027, 0.57735027, 0.57735027, 0.57735027, 0.57735027]]).T),
    (np.array([[0, 0, 0, 1]]).T,
     np.array([[0.57735027, 0.57735027, -0.57735027, -0.57735027, 0.57735027, 0.57735027, -0.57735027, -0.57735027]]).T)
]


def random_az():
    return random() * 2 * pi


def random_el():
    return (random() - 0.5) * pi


@pytest.mark.numpyfile
@pytest.mark.parametrize("order", [0, 1, 2, 3])
class TestCoefs(object):

    def test_is_ndarray(self, order):
        assert type(coefs(random_az(), random_el(), order)) == np.ndarray

    def test_shape(self, order):
        assert coefs(random_az(), random_el(), order).shape == ((order + 1) ** 2,)

    def test_range(self, order):
        result = coefs(random_az(), random_el(), order)
        ones = np.ones(result.shape)
        assert np.all(np.greater_equal(result, ones * -1))
        assert np.all(np.less_equal(result, ones))


@pytest.mark.numpyfile
class TestMatrixForCubeDecode(object):

    def test_is_ndarray(self):
        assert type(matrix_for_cube_decode()) == np.ndarray

    def test_shape(self):
        assert matrix_for_cube_decode(order=1).shape == (8, 4)

    @pytest.mark.parametrize("input_matrix,expected", fixtures)
    def test_decode_1st_order(self, input_matrix: np.ndarray, expected: np.ndarray):
        assert input_matrix.shape == (4, 1)
        mat = matrix_for_cube_decode(order=1)
        decoded = np.dot(mat, input_matrix)
        assert decoded.shape == (8, 1)
        assert expected.shape == (8, 1)
        np.testing.assert_array_almost_equal(decoded, expected)

    @pytest.mark.parametrize("input_matrix,expected", fixtures)
    def test_decode_2nd_order(self, input_matrix: np.ndarray, expected: np.ndarray):
        assert input_matrix.shape == (4, 1)
        mat = matrix_for_cube_decode(order=2)
        decoded = np.dot(mat, np.array([[
            1, 1, 1, 1, 1,
            1, 1, 1, 1
        ]]).T)
        assert decoded.shape == (8, 1)

    @pytest.mark.parametrize("input_matrix,expected", fixtures)
    def test_decode_3rd_order(self, input_matrix: np.ndarray, expected: np.ndarray):
        assert input_matrix.shape == (4, 1)
        mat = matrix_for_cube_decode(order=3)
        decoded = np.dot(mat, np.array([[
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1
        ]]).T)
        assert decoded.shape == (8, 1)


@pytest.mark.numpyfile
class TestDecode(object):

    @pytest.mark.parametrize("input_matrix,expected", fixtures)
    def test_decode(self, input_matrix, expected):
        result = decode(input_matrix, 1)
        assert type(result) == np.ndarray
        assert result.shape == (8, 1)
        np.testing.assert_array_almost_equal(result, expected)
