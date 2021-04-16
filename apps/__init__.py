"""
This file register the dash apps.

If adding more dash apps, you need to change this file as well.
"""

import dash
import dash_bootstrap_components as dbc
from flask import Flask

from apps.constants import HTML_APP_LATENCY_PATH, HTML_APP_DEMO_SLIDER_PATH
from config import Config


def create_app():
    server = Flask(__name__)
    server.config.from_object(Config)

    register_dashapps(server)
    register_blueprints(server)

    return server


# modify when adding more Dash apps
def register_dashapps(app):
    from apps.dashapp_latency.layout import latency_layout
    from apps.dashapp_latency.callbacks import register_latency_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    # the first Dash app
    dashapp_latency = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],   # bootstrap theme
        server=app,
        url_base_pathname=HTML_APP_LATENCY_PATH,  # the access address is at `$homepage_url/HTML_APP_LATENCY_PATH`
        meta_tags=[meta_viewport]
    )

    with app.app_context():
        dashapp_latency.title = 'Dashapp for latency'
        dashapp_latency.layout = latency_layout
        register_latency_callbacks(dashapp_latency)

    # the second Dash app
    from apps.dashapp_demo_slider.layout import demo_slider_layout
    from apps.dashapp_demo_slider.callbacks import register_demo_slider_callbacks

    dashapp_demo_slider = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],  # bootstrap theme
        server=app,
        url_base_pathname=HTML_APP_DEMO_SLIDER_PATH,
        meta_tags=[meta_viewport]
    )

    with app.app_context():
        dashapp_demo_slider.title = 'Dashapp for demo slider'
        dashapp_demo_slider.layout = demo_slider_layout
        register_demo_slider_callbacks(dashapp_demo_slider)

    # register more Dash apps here


def register_blueprints(server):  # do not change
    from apps.routes import server_bp
    server.register_blueprint(server_bp)
