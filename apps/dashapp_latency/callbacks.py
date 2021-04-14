from dash.dependencies import Input
from dash.dependencies import Output

from .plotly_barchart_helper import get_latency_figure_obj


def register_callbacks(dashapp):
    @dashapp.callback(Output('latency-center-chart', 'figure'), [Input('latency-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        return get_latency_figure_obj(selected_dropdown_value)