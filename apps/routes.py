from flask import render_template
from flask import Blueprint

from .constants import HTML_APP_LATENCY_PATH

server_bp = Blueprint('main', __name__)


@server_bp.route("/")
def get_page_home():
    """Home page."""
    return render_template(
        "index.html",    # a html page under "./templates"
        app_latency_title="Latency Charts",
        app_latency_description="Display the latency success rates of the FLASHFlux v3c/v4a SSF Aqua/Terra and the "
                                "TISA data products by month or by year.",
        app_latency_path=HTML_APP_LATENCY_PATH
    )


@server_bp.route("/about")
def get_page_about():
    """Home page."""
    return render_template(
        "about.html",    # a html page under "./templates"
    )
