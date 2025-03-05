import pytest
from python_module_template.functions import divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 2, 2),
        (9, 3, 3),
        (5, 2, 2.5),
        (1, 1, 1),
        (0, 1, 0),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(1, 0)
