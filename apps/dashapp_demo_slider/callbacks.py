"""
The callback function of the demo slider app.

The core part is a Dash slider.
Refer to https://dash.plotly.com/dash-core-components/slider for details.
"""
from dash.dependencies import Input, Output

from .constants import TRACE_DAYS

# some online free pictures
RANDOM_IMAGE_URLS = [  # urls of 7 mock images
    "http://images-assets.nasa.gov/image/PIA17680/PIA17680~orig.jpg",
    "http://images-assets.nasa.gov/image/PIA18156/PIA18156~orig.jpg",
    "http://images-assets.nasa.gov/image/PIA18795/PIA18795~orig.jpg",
    "http://images-assets.nasa.gov/image/PIA02816/PIA02816~orig.jpg",
    "http://images-assets.nasa.gov/image/PIA00948/PIA00948~orig.jpg",
    "http://images-assets.nasa.gov/image/PIA01252/PIA01252~orig.jpg",
    "http://images-assets.nasa.gov/image/PIA04596/PIA04596~orig.jpg"
]


# the callback function of the slider in
def register_demo_slider_callbacks(dashapp):
    @dashapp.callback(  # multiple outputs, single input
        Output('demo-slider-center-img', 'src'),   # return the src of the image
        Output('demo-slider-output-container', 'children'),
        [Input('demo-slider-slider', 'value')]
    )
    def update_output(selected_delta_value: int):
        """
        A mock callback function to return different images based on the slider input value.
        :param selected_delta_value: input, int, in the range [-6, 0] here.
        :return: the image url address, and the input slider value.
        """
        # TODO: replace this with true figures or Plotly figure objects
        return \
            RANDOM_IMAGE_URLS[selected_delta_value + TRACE_DAYS - 1], \
            'You have selected "{}", the data type is {}'.format(selected_delta_value, type(selected_delta_value))
