"""
This file register the dash apps.

If adding more dash apps, you need to change this file as well.
"""

import dash
import dash_bootstrap_components as dbc
from flask import Flask

from apps.constants import HTML_APP_LATENCY_PATH
from config import Config


def create_app():
    server = Flask(__name__)
    server.config.from_object(Config)

    register_dashapps(server)
    register_blueprints(server)

    return server


def register_dashapps(app):
    from apps.dashapp_latency.layout import layout
    from apps.dashapp_latency.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    # the first dash app
    dashapp_latency = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],   # bootstrap theme
        server=app,
        url_base_pathname=HTML_APP_LATENCY_PATH,  # the access address is at `$homepage_url/HTML_APP_LATENCY_PATH`
        meta_tags=[meta_viewport]
    )

    with app.app_context():
        dashapp_latency.title = 'Dashapp for latency'
        dashapp_latency.layout = layout
        register_callbacks(dashapp_latency)

    # TODO: add demo apps


def register_blueprints(server):
    from apps.routes import server_bp
    server.register_blueprint(server_bp)
