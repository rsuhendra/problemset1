import pytest
from reference import *

def test_trans_f_function():
    A = np.array([[1, 4, -1],
                  [0, 7, 1],
                  [1, 7, 2]])

    B = np.array([[1, 2, 6],
                  [1, -7, 3],
                  [0, 1, 2]])

    y_correct = np.array([[5, 7, 8],
                          [-27, -48, -45],
                          [16, 23, 31]])

    AB_T, B_TA_T, diff = trans_f(A, B)

    assert np.array_equal(AB_T, y_correct)
    assert np.array_equal(B_TA_T, y_correct)
    assert np.array_equal(diff, np.zeros((3, 3)))
    
	# tol = 1e-12 
	# assert np.allclose(AB_T, y_correct, atol=tol)
    # assert np.allclose(B_TA_T, y_correct, atol=tol)
    # assert np.allclose(diff, np.zeros((3, 3)), atol=tol)