"""
The callback function of the latency Dash app.

The core part is a Dash dropdown.
Refer to https://dash.plotly.com/dash-core-components/dropdown for details.
"""

from dash.dependencies import Input, Output

from .plotly_barchart_helper import get_latency_figure_obj


# the callback function of the dropdown in layout.py.
# Note the quoted names should be identical to those in layout.py
def register_latency_callbacks(dashapp):
    @dashapp.callback(Output('latency-center-chart', 'figure'), [Input('latency-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        return get_latency_figure_obj(selected_dropdown_value)
