import dash
from dash import html, dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout of the app
app.layout = html.Div([
    dcc.Graph(id='stadium-track'),
    dcc.Slider(
        id='position-slider',
        min=1,
        max=100,
        value=1,
        marks={i: str(i) for i in range(1, 101, 10)},
        step=1
    ),
    html.Div(id='slider-output-container')
])

# Define the callback to update the track and tractor position
@app.callback(
    Output('stadium-track', 'figure'),
    Output('slider-output-container', 'children'),
    [Input('position-slider', 'value')]
)
def update_track(position):
    # Stadium shape track parameters
    straight_length = 2
    radius = 1
    theta = np.linspace(0, 2*np.pi, 100)

    # Track coordinates
    x = np.concatenate((np.linspace(-straight_length, straight_length, 50),
                        straight_length + radius * np.cos(theta),
                        np.linspace(straight_length, -straight_length, 50),
                        -straight_length + radius * np.cos(theta + np.pi)))
    y = np.concatenate((radius * np.ones(50),
                        radius * np.sin(theta),
                        -radius * np.ones(50),
                        radius * np.sin(theta + np.pi)))

    # Tractor position on the track
    tractor_x = x[position - 1]
    tractor_y = y[position - 1]

    # Create figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Track'))
    fig.add_trace(go.Scatter(x=[tractor_x], y=[tractor_y], mode='markers', name='Tractor'))

    # Update layout
    fig.update_layout(showlegend=False, xaxis_showgrid=False, yaxis_showgrid=False,
                      xaxis_zeroline=False, yaxis_zeroline=False)
    
    return fig, f'Position: {position}'

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
