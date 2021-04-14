"""
The layout of the latency dash app.

"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from .constants import OPTION_STR
from apps.constants import HTML_RETURN_BUTTON

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

CENTER_GRAPH = dbc.Card(  # the center chart in a Bootstrap Card
    [
        # Below are all Dash.html components
        # Ref: https://dash.plotly.com/dash-html-components

        EXPLANATION_TXT,
        html.Hr(),

        # title of the drop-down
        html.H4('Select a data source'),
        # dropdown area
        dcc.Dropdown(
            id='latency-dropdown',
            options=[{'label': type_str, 'value': type_str} for type_str in OPTION_STR],
            value='Aqua'  # set default value as "Aqua"
        ),
        # a blank line
        html.Br(),
        # graph area
        dcc.Graph(id="latency-center-chart"),  # id the same as that in its callback function
    ],
    body=True,
)


layout = dbc.Container(
    [
        html.Br(),
        html.H2("Latency Success Rates"),  # page title
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(CENTER_GRAPH),
            ],
            align="center",
        ),
        html.Br(),
        html.Hr(),
        HTML_RETURN_BUTTON,
    ],
    fluid=False,   # False indicates there is a center box which will not expand when the screen is too wide
)
