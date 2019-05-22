import numpy
import plotly.plotly
import plotly.graph_objs as go

from playground.utils.math_utils import (
    get_circumference_points_origin_zero,
    signal_vector,
)
from playground.utils.plot_utils import (
    get_scatter_from_circumference,
    get_scatter_from_vector,
)


# Common data
frequency = 4
sample_rate = 200
x = numpy.arange(sample_rate)
time = x / sample_rate

# Signal 1
amplitude = 1
phase = 0
sample_rate = amplitude / 100

vector_1 = signal_vector(phase, amplitude)
circunference_range_1 = numpy.arange(
    -amplitude,
    amplitude + sample_rate,
    sample_rate,
)
circumference_vector_1 = get_circumference_points_origin_zero(
    radius=amplitude,
    sample_range=circunference_range_1,
)

# Signal 2
amplitude2 = 2
phase2 = 90
sample_rate2 = amplitude2 / 100

vector_2 = signal_vector(phase2, amplitude2)
circunference_range_2 = numpy.arange(
    -amplitude2,
    amplitude2 + sample_rate2,
    sample_rate2,
)
circumference_vector_2 = get_circumference_points_origin_zero(
    radius=amplitude2,
    sample_range=circunference_range_2,
)

# Signal 3
amplitude3 = 2
phase3 = 45
sample_rate3 = amplitude3 / 100

vector_3 = signal_vector(phase3, amplitude3)
circunference_range_3 = numpy.arange(
    -amplitude3,
    amplitude3 + sample_rate3,
    sample_rate3,
)
circumference_vector_3 = get_circumference_points_origin_zero(
    radius=amplitude3,
    sample_range=circunference_range_3,
)

scatter_vector_1 = get_scatter_from_vector(
    vector=vector_1,
    name='Signal 1',
)
scatter_circumference_1 = get_scatter_from_circumference(
    circumference_vector_1,
    name='Signal 1'
)
scatter_vector_2 = get_scatter_from_vector(
    vector=vector_2,
    name='Signal 2',
)
scatter_circumference_2 = get_scatter_from_circumference(
    circumference_vector_2,
    name='Signal 2'
)
scatter_vector_3 = get_scatter_from_vector(
    vector=vector_3,
    name='Signal 3',
)
scatter_circumference_3 = get_scatter_from_circumference(
    circumference_vector_3,
    name='Signal 3'
)

fig = go.Figure(
    data=[
        scatter_vector_1,
        scatter_circumference_1,
        scatter_vector_2,
        scatter_circumference_2,
        scatter_vector_3,
        scatter_circumference_3,
    ],
    layout=go.Layout(
        title='Vectorial domain',
        xaxis={
            'domain': [0, 1],
        },
        yaxis={
            'domain': [0, 1],
        },
        width=700,
        height=700,
    )
)
plotly.offline.plot(
    fig,
    filename='plot_2_vectorial_domain',
    auto_open=True,
)
