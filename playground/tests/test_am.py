import pytest

from playground.utils.am import amplitude_modulation


TIME_ZERO = 0
TIME_025 = 0.25
TIME_05 = 0.5
TIME_058 = 0.58
TIME_075 = 0.75
TIME_092 = 0.92
TIME_1 = 1
EXPECTED = [
    (TIME_ZERO, 0),
    (TIME_025, 2),
    (TIME_05, 0),
    (TIME_058, -0.25),
    (TIME_075, 0),
    (TIME_092, -0.25),
    (TIME_1, 0),
]


@pytest.mark.parametrize('x_time,expected', EXPECTED)
def test_amplitud_modulation(x_time, expected):

    am_args = {
        'ac': 1,
        'am': 1,
        'fc': 1,
        'fm': 1,
        'time': x_time,
    }
    y = amplitude_modulation(**am_args)

    assert pytest.approx(y, rel=1e-1) == expected
