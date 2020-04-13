import numpy as np
from .normalize_conversion import convert_fuma_to_ambix_3rd_order
from math import sqrt
import pytest


class TestConvertFumaToAmbiX(object):

    @pytest.mark.parametrize(  # type: ignore
        'fuma',
        [
            np.ones((16,)),
            np.array(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) * 0.01
        ]
    )
    def test_convert_3rd_order(self, fuma: np.ndarray) -> None:
        converted = convert_fuma_to_ambix_3rd_order(fuma)
        assert converted.shape
        np.testing.assert_array_almost_equal(
            converted,
            [
                sqrt(2) * fuma[0],
                fuma[2],
                fuma[3],
                fuma[1],
                sqrt(3 / 4) * fuma[8],
                sqrt(3 / 4) * fuma[6],
                fuma[4],
                sqrt(3 / 4) * fuma[5],
                sqrt(3 / 4) * fuma[7],
                sqrt(5 / 8) * fuma[15],
                sqrt(5 / 9) * fuma[13],
                sqrt(32 / 45) * fuma[11],
                fuma[9],
                sqrt(32 / 45) * fuma[10],
                sqrt(5 / 9) * fuma[12],
                sqrt(5 / 8) * fuma[14]
            ]
        )
