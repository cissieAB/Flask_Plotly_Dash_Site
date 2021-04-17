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
from apps.dashapp_demo_slider.constants import TRACE_DAYS
from apps.dashapp_demo_slider.get_most_recent_dates import MOST_RECENT_SEVEN_DATES

EXPLANATION_TXT = html.Div(
    [
        dcc.Markdown('''
        This is a demo for the Dash slider.
        
        Now it displays 7 different images according to the slider input values.
        
        Replace the images with other static images or the Plotly figure objects.
        '''),
    ]
)

center_area = dbc.Card(  # the center area is wrapped by a Bootstrap Card
    [
        # Below are all Dash.html components
        # Ref: https://dash.plotly.com/dash-html-components

        EXPLANATION_TXT,
        html.Hr(),

        # center area
        # dcc.Graph(),   # use this when the object is a Plotly figure
        html.Img(
            id="demo-slider-center-img",
            style={
                'width': '80%',
                'margin-bottom': 40,
                'display': 'block',   # center the image
                'margin-left': 'auto',
                'margin-right': 'auto',
            }
        ),  # make sure id the same as that in its callback function

        # slider here, core part
        # 7 dates from left to right, represented by [-6.5, 0.5]
        # the most recent date is at the rightmost position
        dcc.Slider(
            id='demo-slider-slider',   # make sure id the same as that in its callback function
            min=0.5 - TRACE_DAYS,
            max=0.5,
            step=1,   # step size of each slide, 1 day here
            value=0,  # default value, at the most recent date
            marks={i + 1 - TRACE_DAYS: MOST_RECENT_SEVEN_DATES[i] for i in range(TRACE_DAYS)},  # date strings
        ),

        # a blank line
        html.Br(),
        # a reminder bar, delete this when needed
        html.Div(id='demo-slider-output-container', style={'margin-top': 20}),  # display the true slider value
    ],
    body=True,
)


demo_slider_layout = get_app_main_container(HTML_APP_DEMO_SLIDER_TITLE, center_area)
