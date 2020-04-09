import numpy as np
import pytest
from generate_matrix import div


@pytest.mark.numpyfile
class TestNumpy(object):
    """ check approximate-equalilty conditions using numpy.testing """

    def test_div_pytest(self):
        # 0.66667 != 0.6666666666666666
        assert div(2, 3) != 0.66667

    def test_dif2Num_numpy_4places(self):
        #  2/3 = 0.6666666666666666 = 0.66667 i.e. equal upto 4 places
        np.testing.assert_approx_equal(div(2, 3), 0.66667, 4)

    def test_dif2Num_numpy_5places(self):
        # 2/3 = 0.6666666666666666 = 0.66667 i.e. equal upto 5 places
        # note that it is round off for last value i.e.
        # 0.6666666666666666 is changed to 0.66667 before comparision
        np.testing.assert_approx_equal(div(2, 3), 0.66667, 5)

    @pytest.mark.skip
    def test_dif2Num_numpy_6places(self):
        # failed because
        # 2/3 = 0.6666666666666666 = 0.666667 != 0.666668 upto 6 places
        np.testing.assert_approx_equal(div(2, 3), 0.666668, 6)
