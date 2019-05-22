import numpy
import plotly.plotly
import plotly.graph_objs as go

from utils.am import amplitude_modulation
from utils.math_utils import sinusoide


Ac = 5  # 5V
Am = 2  # 2V
Fc = 8  # 80KHz
Fm = 0.4  # 40Hz

time = numpy.arange(start=0, stop=10, step=0.01)

modulated = go.Scatter(
    x=time,
    y=amplitude_modulation(Ac, Am, Fc, Fm, time),
    name='AM',
)

carrier = go.Scatter(
    x=time,
    y=sinusoide(Ac, Fc, time, phase=0),
    name='Carrier',
)

m_envelope = go.Scatter(
    x=time,
    y=sinusoide(Am, Fm, time, phase=0) + Ac,
    name='M',
)
m_envelope_2 = go.Scatter(
    x=time,
    y=sinusoide(Am, Fm, time, phase=0) * -1 + Ac * -1,
    name='M2',
)

plotly.offline.plot(
    [modulated, m_envelope, m_envelope_2],
    filename='am_testing',
    auto_open=True,
)
