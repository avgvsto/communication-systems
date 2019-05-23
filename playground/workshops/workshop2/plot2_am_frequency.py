import numpy
import plotly.plotly
import plotly.graph_objs as go

from playground.utils.plot_utils import get_scatter_from_vector


Ac = 5  # 5V
Am = 2  # 2V
Fc = 8  # 8Hz
Fm = 0.4  # 0.4Hz

frequency = numpy.arange(start=6, stop=10, step=1)

go.Scatter(
    x=[6, 7, Fc, 9, 10],
    y=[0, 0, Ac, 0, 0],
    name='Carrier',
)
carrier_vector = ((Fc, 0), (Fc, Ac))
scatter_carrier = get_scatter_from_vector(
    vector=carrier_vector,
    name='Carrier',
)

f_lower_sideband = Fc - Fm
lower_sideband_vector = ((f_lower_sideband, 0), (f_lower_sideband, Am))
scatter_lower_sideband = get_scatter_from_vector(
    vector=lower_sideband_vector,
    name='Lower sideband',
)

f_upper_sideband = Fc + Fm
upper_sideband_vector = ((f_upper_sideband, 0), (f_upper_sideband, Am))
scatter_upper_sideband = get_scatter_from_vector(
    vector=upper_sideband_vector,
    name='Upper sideband',
)

figure = go.Figure(
    data=[
        scatter_carrier,
        scatter_lower_sideband,
        scatter_upper_sideband,
    ],
    layout=go.Layout(
        title='Modulated amplitude - frequency domain',
        xaxis={
            'title': 'frequency (Hz)',
        },
        yaxis={
            'title': 'A (V)',
        },
    )
)
plotly.offline.plot(
    figure,
    filename='w2_p2_frequency',
    auto_open=True,
)
