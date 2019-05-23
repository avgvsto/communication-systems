import numpy
import plotly.plotly
import plotly.graph_objs as go

from playground.utils.am import amplitude_modulation
from playground.utils.math_utils import sinusoide


Ac = 5  # 5V
Am = 2  # 2V
Fc = 8  # 8Hz
Fm = 0.4  # 0.4Hz

time = numpy.arange(start=0, stop=10, step=0.01)

modulated = go.Scatter(
    x=time,
    y=amplitude_modulation(Ac, Am, Fc, Fm, time),
    name='Modulated signal',
)

carrier = go.Scatter(
    x=time,
    y=sinusoide(Ac, Fc, time, phase=0),
    name='Carrier',
)

m_envelope = go.Scatter(
    x=time,
    y=sinusoide(Am, Fm, time, phase=0) + Ac,
    name='Envelope (A message + A carrier)',
)
m_envelope_2 = go.Scatter(
    x=time,
    y=(sinusoide(Am, Fm, time, phase=0) + Ac) * -1,
    name='Envelope (A message + A carrier) * -1',
)

figure = go.Figure(
    data=[modulated, m_envelope, m_envelope_2, carrier],
    layout=go.Layout(
        title='Modulated amplitude',
        xaxis={'title': 'time (s)'},
        yaxis={'title': 'A (V)'},
    ),
)
plotly.offline.plot(
    figure,
    filename='am_testing',
    auto_open=True,
)
