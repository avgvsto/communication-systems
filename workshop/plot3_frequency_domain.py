import plotly.plotly
import plotly.graph_objs as go


# Common data
frequency = 4

# Signal 1
amplitude = 1

# Signal 2
amplitude2 = 2

# Signal 3
amplitude3 = 2

signal_1 = go.Scatter(
    x=[frequency, frequency],
    y=[0, amplitude],
    name='Signal 1'
)
signal_2 = go.Scatter(
    x=[frequency, frequency],
    y=[0, amplitude2],
    name='Signal 2'
)
signal_3 = go.Scatter(
    x=[frequency, frequency],
    y=[0, amplitude3],
    name='Signal 3'
)

data = [
    signal_1,
    signal_2,
    signal_3,
]

plotly.offline.plot(
    data,
    filename='plot_3_frequency_domain',
    auto_open=True,
)
