import numpy as np
import pytest
from .generate_matrix import matrix_for_cube_decode, coefs, decode
from math import pi, sqrt
from random import random
from .type_definitions import Rad, TestData
from .test_data import data_for_decode_test


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
        a = sqrt(1 / 3)
        np.testing.assert_array_almost_equal(
            mat,
            np.array([
                [1, a, -a, a],
                [1, -a, -a, a],
                [1, a, -a, -a],
                [1, -a, -a, -a],
                [1, a, a, a],
                [1, -a, a, a],
                [1, a, a, -a],
                [1, -a, a, -a]
            ]),
            decimal=12
        )

    def test_decode_2nd_order(self) -> None:
        mat = matrix_for_cube_decode(order=2)
        assert type(mat) == np.ndarray
        assert mat.shape == (8, 9)
        a = sqrt(1 / 3)
        np.testing.assert_array_almost_equal(
            mat,
            np.array([
                [1, a, -a, a, a, -a, 0, -a, 0],
                [1, -a, -a, a, -a, a, 0, -a, 0],
                [1, a, -a, -a, -a, -a, 0, a, 0],
                [1, -a, -a, -a, a, a, 0, a, 0],
                [1, a, a, a, a, a, 0, a, 0],
                [1, -a, a, a, -a, -a, 0, a, 0],
                [1, a, a, -a, -a, a, 0, -a, 0],
                [1, -a, a, -a, a, -a, 0, -a, 0]

            ]),
            decimal=12
        )

    def test_decode_3rd_order(self) -> None:
        mat = matrix_for_cube_decode(order=3)
        assert type(mat) == np.ndarray
        assert mat.shape == (8, 16)
        a = sqrt(1 / 3)
        b = sqrt(5 / 54)
        c = sqrt(5 / 9)
        d = sqrt(1 / 18)
        e = sqrt(4 / 27)
        np.testing.assert_array_almost_equal(
            mat,
            np.array([
                [1, a, -a, a, a, -a, 0, -a, 0, b, -c, d, e, d, 0, -b],
                [1, -a, -a, a, -a, a, 0, -a, 0, -b, c, -d, e, d, 0, -b],
                [1, a, -a, -a, -a, -a, 0, a, 0, b, c, d, e, -d, 0, b],
                [1, -a, -a, -a, a, a, 0, a, 0, -b, -c, -d, e, -d, 0, b],
                [1, a, a, a, a, a, 0, a, 0, b, c, d, -e, d, 0, -b],
                [1, -a, a, a, -a, -a, 0, a, 0, -b, -c, -d, -e, d, 0, -b],
                [1, a, a, -a, -a, a, 0, -a, 0, b, -c, d, -e, -d, 0, b],
                [1, -a, a, -a, a, -a, 0, -a, 0, -b, c, -d, -e, -d, 0, b]

            ]),
            decimal=12
        )


class TestDecode(object):

    @pytest.mark.parametrize("test_data", data_for_decode_test)  # type: ignore
    def test_decode(self, test_data: TestData) -> None:
        order = test_data.order
        assert test_data.input.shape == ((order + 1) ** 2, 1)
        result = decode(test_data.input, test_data.order)
        assert type(result) == np.ndarray
        assert result.shape == (8, 1)
        assert test_data.decoded.shape == (8, 1)
        np.testing.assert_array_almost_equal(result, test_data.decoded)
