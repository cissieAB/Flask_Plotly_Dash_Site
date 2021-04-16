"""
The layout for the demo_slider app.

The core part is a Dash slider.
Refer to https://dash.plotly.com/dash-core-components/slider for details.
"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from apps.common_app_layouts import get_app_main_container
from apps.constants import HTML_APP_DEMO_SLIDER_TITLE

EXPLANATION_TXT = html.Div(
    [
        dcc.Markdown('''
        This is a demo for the Dash slider.
        '''),
    ]
)

center_graph = dbc.Card(  # the center chart in a Bootstrap Card
    [
        # Below are all Dash.html components
        # Ref: https://dash.plotly.com/dash-html-components

        EXPLANATION_TXT,
        html.Hr(),

        # graph area
        # dcc.Graph(id="demo-slider-center-chart"),  # make sure id the same as that in its callback function

        # slider here, core part
        dcc.Slider(
            id='demo-slider-slider',   # make sure id the same as that in its callback function
            min=0,
            max=6,
            step=1,   # step size of each slide
            value=0,  # default value
        ),
        # a blank line
        html.Br(),
        html.Div(id='demo-slider-output-container'),
    ],
    body=True,
)


demo_slider_layout = get_app_main_container(HTML_APP_DEMO_SLIDER_TITLE, center_graph)
