"""
The layout of the latency dash app.
Most of the context is static written with HTML or Markdown.

The core part is a Dash dropdown. Refer to https://dash.plotly.com/dash-core-components/dropdown for details.
"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from .constants import OPTION_STR
from apps.common_app_layouts import get_app_main_container

# some explanation texts
EXPLANATION_TXT = html.Div(
    [
        dcc.Markdown('''
        We define a data product to be a **"success"** if its processed result is released in a threshold of days. 
        For SSF Aqua/Terra, the target is within 3 or 4 days. For TISA, the target is within 6 or 7 days. 
        If the latency of a particular date is within the target, this day is considered to be a "success". 
        '''),

        dcc.Markdown('''
        The FLASHFlux data has two versions: **v3C** and **v4A**. 
        The v3C data includes dates from Aug-2017 to Aug-2020. 
        The v4A data begins at Sep-2020. 
        '''),

        dcc.Markdown('''
        In the following, we provide the latency success rate statistics of:
        * Aqua: the *monthly* latency success rates of SSF Aqua data from Aug-2017 to current, of both v3C and v4A;
        * Terra: the *monthly* latency success rates of SSF Terra data from Aug-2017 to current, of both v3C and v4A;
        * TISA: the *monthly* latency success rates of SSF Terra data from Aug-2017 to current, of both v3C and v4A;
        * All: The *yearly* latency success rates of the Aqua/Terra/TISA data from Aug-2017 to current. 
        v3C and v4A data are separated into two figures.
        '''),
    ]
)

center_area = dbc.Card(  # the center chart in a Bootstrap Card
    [
        # Below are all Dash.html components
        # Ref: https://dash.plotly.com/dash-html-components

        EXPLANATION_TXT,
        html.Hr(),

        # title of the drop-down
        html.H4('Select a data source'),
        # dropdown area, core part
        dcc.Dropdown(
            id='latency-dropdown',   # make sure id the same as that in its callback function
            options=[{'label': type_str, 'value': type_str} for type_str in OPTION_STR],
            value='Aqua'  # set default value as "Aqua"
        ),
        # a blank line
        html.Br(),
        # graph area
        dcc.Graph(id="latency-center-chart"),  # make sure id the same as that in its callback function
    ],
    body=True,
)

app_title_txt = "Latency Success Rates"
layout = get_app_main_container(app_title_txt, center_area)
