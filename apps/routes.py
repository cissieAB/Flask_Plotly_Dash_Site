"""
This file defines the structure of the website and their routes.

Up to April 2021, only two pages are supported.
One is the homepage at $homepage_url$
The other is the about page at $homepage_url$/about.

You can add more pages following the Flask routing rules at
https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing.
"""

from flask import render_template
from flask import Blueprint

from .constants import HTML_APP_LATENCY_PATH

server_bp = Blueprint('main', __name__)


@server_bp.route("/")
def render_page_home():
    """Render the homepage."""
    return render_template(
        "index.html",    # a html file at "./templates"
        # parameters for the first dash app
        app_1_latency_title="Latency Charts",
        app_1_latency_description="Display the latency success rates of the FLASHFlux v3c/v4a SSF Aqua/Terra and the "
                                "TISA data products by month or by year.",
        app_1_latency_path=HTML_APP_LATENCY_PATH
    )


@server_bp.route("/about")
def render_page_about():
    """Render the page at homepage_url/about. Refer this to create more static pages."""
    return render_template(
        "about.html",    # a html file at "./templates"
    )
