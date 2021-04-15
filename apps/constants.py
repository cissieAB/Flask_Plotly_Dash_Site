"""
Defines the url addresses for the dash apps.
Also defines a "return to homepage" button for each dash app page to integrate.
"""

import dash_bootstrap_components as dbc

# url mappings for the dash plot apps
HTML_APP_LATENCY_PATH = "/latency/"
HTML_HOME_PATH = "http://127.0.0.1:5000"   # TODO: currently only supports absolute url address. Seek better solutions

######
# dash-bootstrap constants
######
# a return to homepage button
HTML_RETURN_BUTTON = dbc.Button(
    "Return to home page",
    color="primary",
    href=HTML_HOME_PATH,
    block=True,
)
