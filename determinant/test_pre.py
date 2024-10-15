import pytest
from reference import *

file_name = 'pretest_data.npy'
Asol = np.load(file_name)

def test_pre():
    assert np.array_equal(A, Asol)
