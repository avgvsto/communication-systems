import math
import numpy


def sinusoide(amplitude, frequency, time, phase):

    return amplitude * numpy.sin(2 * numpy.pi * frequency * time + numpy.radians(phase))


def signal_vector(phase, amplitude):

    # Getting the signal vector through Pythagoras
    x = amplitude * numpy.cos(numpy.radians(phase))
    y = amplitude * numpy.sin(numpy.radians(phase))

    initial_point = (0, 0)
    final_point = (x, y)

    return initial_point, final_point


def get_circumference_y(radius, x):

    # Circumference with origin in zero.
    # x^2 + y^2 = r^2
    #
    # E.g:
    # 0^2 + y^2 = 3^2
    # 0 + y^2 = 9
    # y = sqrt(9)
    # y = 3

    step_1 = math.pow(radius, 2) - math.pow(x, 2)

    if step_1 < 0:
        y = -math.sqrt(-step_1)
    else:
        y = math.sqrt(step_1)

    return y


def get_circumference_points_origin_zero(radius, sample_range):

    x_range = list(reversed([x for x in sample_range]))
    positive_half = [(x, get_circumference_y(radius, x)) for x in x_range]
    negative_half = []
    for point in list(reversed(positive_half[:-1])):
        negative_half.append((point[0], -point[1]))

    points = positive_half + negative_half

    return points
