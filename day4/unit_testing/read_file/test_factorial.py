import pytest
from scipy.special import gamma, factorial

# Run tests
@pytest.mark.parametrize(
    ("n", "value"), [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720)]
)
def test_factorial(n, value):

    assert gamma(n + 1) == value
