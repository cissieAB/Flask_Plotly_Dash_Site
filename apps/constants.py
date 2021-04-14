import dash_bootstrap_components as dbc

# A path file for html page addresses
HTML_APP_LATENCY_PATH = "/latency/"
HTML_HOME_PATH = "http://127.0.0.1:5000"   # TODO: currently only supports absolute url address

# dbc constants   #
HTML_RETURN_BUTTON = dbc.Button(
    "Return to home page",
    color="primary",
    href=HTML_HOME_PATH,
    block=True,
)
