# -*- coding: utf-8 -*-

import unittest
import numpy as np
from numpy.testing import assert_array_equal
from numpy.testing import assert_array_almost_equal
from pyStratAlpha.maths.matrix import eig_val_pct
from pyStratAlpha.maths.matrix import pca_decomp


class TestMatrix(unittest.TestCase):
    def testEigValPct(self):
        eig_vals = [5.0, 2.0, 3.0, 10.0, 4.0, 15.0]
        percentage = [0.0, 0.5, 0.99, 1.0]
        calculated = [eig_val_pct(eig_vals, pct=pct) for pct in percentage]
        expected = [1, 2, 6, 6]
        np.testing.assert_array_equal(calculated, expected)

    def testPcaDecomp(self):
        x = [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1]
        y = [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9]
        data_mat = np.array([x, y])
        data_mat = data_mat.T
        lwo_dim_mat, recon_mat = pca_decomp(data_mat, pct=0.5)
        expected_low_dim_mat = np.array([[-0.82797019],
                                        [1.77758033],
                                        [-0.99219749],
                                        [-0.27421042],
                                        [-1.67580142],
                                        [-0.9129491],
                                        [0.09910944],
                                        [1.14457216],
                                        [0.43804614],
                                        [1.22382056]])
        expected_recon_mat = np.array([[2.37125896, 2.51870601],
                                     [0.60502558, 0.60316089],
                                     [2.48258429, 2.63944242],
                                     [1.99587995, 2.11159364],
                                     [2.9459812, 3.14201343],
                                     [2.42886391, 2.58118069],
                                     [1.74281635, 1.83713686],
                                     [1.03412498, 1.06853498],
                                     [1.51306018, 1.58795783],
                                     [0.9804046, 1.01027325]])
        assert_array_almost_equal(lwo_dim_mat, expected_low_dim_mat)
        assert_array_almost_equal(recon_mat, expected_recon_mat)
