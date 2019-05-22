import plotly.graph_objs as go


def get_scatter_from_vector(vector, name):

    initial_point = vector[0]
    final_point = vector[1]

    if len(initial_point) != len(final_point):
        raise Exception('Vector dimensions do not match!')

    x, y = [x for x in zip(initial_point, final_point)]
    scatter = go.Scatter(
        x=x,
        y=y,
        name=name,
    )

    return scatter


def get_scatter_from_circumference(circumference, name):

    x, y = [point for point in zip(*circumference)]
    scatter = go.Scatter(
        x=x,
        y=y,
        name=name,
        line={
            'width': 1,
            'dash': 'dot',
        },
    )

    return scatter
