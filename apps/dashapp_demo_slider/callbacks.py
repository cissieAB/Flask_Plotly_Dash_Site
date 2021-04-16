"""
The callback function of the demo slider app.

The core part is a Dash slider.
Refer to https://dash.plotly.com/dash-core-components/slider for details.
"""

from dash.dependencies import Input
from dash.dependencies import Output


# the callback function of the slider in
def register_demo_slider_callbacks(dashapp):
    @dashapp.callback(Output('demo-slider-output-container', 'children'), [Input('demo-slider-slider', 'value')])
    def update_output(value):
        return 'You have selected "{}"'.format(value)
