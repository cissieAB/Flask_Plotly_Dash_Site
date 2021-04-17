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

from .constants import *

server_bp = Blueprint('main', __name__)


@server_bp.route("/")
def render_page_home():
    """Render the homepage."""
    return render_template(
        "index.html",    # a html file at "./templates"
        # parameters for the first Dash app
        app_1_latency_title=HTML_APP_LATENCY_TITLE,
        app_1_latency_description="Display the latency success rates of the FLASHFlux v3c/v4a SSF Aqua/Terra and the "
                                  "TISA data products by month or by year.",
        app_1_latency_path=HTML_APP_LATENCY_PATH,
        # parameters for the second Dash app
        app_2_demo_slider_title=HTML_APP_DEMO_SLIDER_TITLE,
        app_2_demo_slider_description="A demo for the Dash slider representing 7 days. "
                                      "Show different pictures according to different slider input values.",
        app_2_demo_slider_path=HTML_APP_DEMO_SLIDER_PATH,
        # parameters for the third Dash app
        app_3_title="Plot 3",
        app_3_description="Description text written in `routes.py` goes here."
                          " Change the href of the below button after the app is created.",
        app_3_path=HTML_HOME_PATH,
    )


@server_bp.route("/about")
def render_page_about():
    """Render the page at homepage_url/about. Refer this to create more static pages."""
    return render_template(
        "about.html",    # a html file at "./templates"
    )
