"""
The common layouts for the Dash app pages.
"""

import dash_bootstrap_components as dbc
import dash_html_components as html

from .constants import HTML_HOME_PATH

# a return to homepage button
HTML_RETURN_BUTTON = dbc.Button(
    "Return to home page",
    color="primary",
    href=HTML_HOME_PATH,
    block=True,
)


def get_app_main_container(app_title_txt, center_area):
    """
    Build the app page layout according to the app title text and the center area.
    :param app_title_txt: a string, page title
    :param center_area: the main Dash components in the center, containing a graph area and an interactive controller.
    """
    return dbc.Container(
        [
            html.Br(),
            html.H2(app_title_txt),  # page title
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(center_area),
                ],
                align="center",
            ),
            html.Br(),
            html.Hr(),
            HTML_RETURN_BUTTON,
        ],
        fluid=False,  # False indicates there is a center box which will not expand when the screen goes too wide
    )
