import pytest

from workshop.utils.math_utils import (
    get_circumference_points_origin_zero,
    get_circumference_y,
    signal_vector,
)


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ({'radius': 3, 'x': 0}, 3),
        ({'radius': 3, 'x': 3}, 0),
        ({'radius': 3, 'x': -3}, 0),
    ]
)
def test_get_circumference_y(test_input, expected):

    y = get_circumference_y(**test_input)

    assert y == expected


def test_get_circumference_points_origin_zero():

    test_range = range(-3, 4, 3)
    points = get_circumference_points_origin_zero(3, test_range)
    expected = [
        (3, 0),
        (0, 3),
        (-3, 0),
        (0, -3),
        (3, 0),
    ]
    assert points == expected


@pytest.mark.parametrize(
    'test_input,expected_final_point',
    [
        ({'phase': 0, 'amplitude': 2}, (2, 0)),
        ({'phase': 90, 'amplitude': 2}, (0, 2)),
        ({'phase': 180, 'amplitude': 2}, (-2, 0)),
        ({'phase': 270, 'amplitude': 2}, (0, -2)),
        ({'phase': 360, 'amplitude': 2}, (2, 0)),
    ]
)
def test_signal_vector(test_input, expected_final_point):

    initial_point, final_point = signal_vector(**test_input)
    expected_initial_point = (0, 0)

    final_x = round(final_point[0])
    final_y = round(final_point[1])

    assert initial_point == expected_initial_point
    assert (final_x, final_y) == expected_final_point
