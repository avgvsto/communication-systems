import numpy
import plotly.plotly
import plotly.graph_objs as go

from playground.utils.math_utils import sinusoide


frequency = 4
sample_rate = 200
x = numpy.arange(sample_rate)
time = x / sample_rate

# Signal 1
amplitude = 1
phase = 0
y = sinusoide(amplitude, frequency, time, phase)

# Signal 2
amplitude2 = 2
phase2 = 90
y2 = sinusoide(amplitude2, frequency, time, phase2)

# Signal 3
amplitude3 = 2
phase3 = 45
y3 = sinusoide(amplitude3, frequency, time, phase3)

# Resulting signal
amplitude_r = y + y2 + y3

signal_1 = go.Scatter(x=x, y=y, name='Signal 1 (A: 1V, Ph: 0º)')
signal_2 = go.Scatter(x=x, y=y2,  name='Signal 2 (A: 2V, Ph: 90º)')
signal_3 = go.Scatter(x=x, y=y3,  name='Signal 3 (A: 2V, Ph: 45º)')
signal_r = go.Scatter(x=x, y=amplitude_r,  name='Resulting', line={'width': 4})
data = [
    signal_1,
    signal_2,
    signal_3,
    signal_r,
]

figure = go.Figure(
    data=data,
    layout=go.Layout(
        title='Sinoidal functions',
        xaxis={'title': 'time (s)'},
        yaxis={'title': 'A (V)'},
    ),
)
plotly.offline.plot(
    figure,
    filename='plot_1_time_domain',
    auto_open=True,
)
