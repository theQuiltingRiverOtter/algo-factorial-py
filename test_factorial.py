from factorial import factorial, non_r_factorial
import pytest


def test_factorial_small():
    assert factorial(4) == 24


def test_factorial_mid():
    assert factorial(8) == 40320


def test_factorial_large():
    assert factorial(18) == 6402373705728000


def test_factorial_xlarge():
    assert factorial(45) == 119622220865480194561963161495657715064383733760000000000


def test_factorial_error():
    with pytest.raises(TypeError):
        factorial(-1)


def test_non_r_factorial():
    assert non_r_factorial(4) == 24


def test_non_r_factorial_mid():
    assert non_r_factorial(8) == 40320


def test_non_r_factorial_large():
    assert non_r_factorial(18) == 6402373705728000


def test_non_r_factorial_xlarge():
    assert (
        non_r_factorial(45) == 119622220865480194561963161495657715064383733760000000000
    )


def test_non_r_factorial_error():
    with pytest.raises(TypeError):
        non_r_factorial(-1)
