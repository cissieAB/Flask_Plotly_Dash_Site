import plotly.graph_objects as go
from plotly.subplots import make_subplots

from apps.dashapp_latency.get_latency_data import \
    aqua_by_month_data, aqua_by_year_data, \
    tisa_by_month_data, tisa_by_year_data, \
    terra_by_month_data, terra_by_year_data
from apps.dashapp_latency.constants import *

# color names, refer to https://www.w3schools.com/colors/colors_names.asp
# using lower case letters
TISA_BAR_COLORS = ["steelblue", "skyblue"]
TERRA_BAR_COLORS = ["tan", "wheat"]
AQUA_BAR_COLORS = ["mediumaquamarine", "aquamarine"]


class MonthlySubPlotData:
    """
    Create and initialize the data for the monthly latency plot with
    one type and one version.
    """
    def __init__(self, data, type_str, version_str):
        """
        Get the fig data according to the input data
        :param data: self-defined SingleFileMonthlyLatencyData class
        :param type_str: in ["Aqua", "Terra", "TISA"]
        """
        self.x = data.x
        self.y1 = data.y1
        self.y2 = data.y2
        self.legends = [
            version_str + ": " + data.y1_legend_str,
            version_str + ": " + data.y2_legend_str
        ]
        self.colors = self.get_bar_colors(type_str)

    def get_bar_colors(self, type_str):
        if type_str == AQUA:
            return AQUA_BAR_COLORS
        elif type_str == TERRA:
            return TERRA_BAR_COLORS
        elif type_str == TISA:
            return TISA_BAR_COLORS


class MonthlyFigData:
    """
    Create and initialize the data for the monthly latency plot
    of one type of data with Version3C and Version4A.
    """
    def __init__(self):
        self.sub_1_data = None
        self.sub_2_data = None

    def init_data(self, data, type_str):
        """
        Get the plot data according to the input class :param data and :param type_str
        :param data: self-defined class PackedMultiVersionMonthlyLatencyData
        :param type_str: in ["Aqua", "Terra", "TISA"]
        """
        self.sub_1_data = MonthlySubPlotData(data.v3c, type_str, VERSION_STR[0])
        self.sub_2_data = MonthlySubPlotData(data.v4a, type_str, VERSION_STR[1])

    def get_title_str(self, type_str):
        if type_str == TISA:
            return "FLASHFlux TISA Monthly Latency Success Rates"
        else:
            return "FLASHFlux SSF " + type_str + " Monthly Latency Success Rates"


def add_two_bar_traces(fig_obj, sub_plot_data, flag_bar_outline):
    """
    Add two bar traces to the fig obj.
    :param fig_obj: the plotly figure obj
    :param sub_plot_data: data of a single version
    :param flag_bar_outline: the flag for whether the bar is outlined in black color. Now v4A data is outlined.
    """
    fig_obj.add_trace(  # bar 1
        go.Bar(
            x=sub_plot_data.x,
            y=sub_plot_data.y1,
            name=sub_plot_data.legends[0],
            marker_color=sub_plot_data.colors[0],
            marker_line_color="black" if flag_bar_outline else sub_plot_data.colors[0],
            marker_line_width=1.5 if flag_bar_outline else 0,
            width=0.7,   # double the width of the second bar
            opacity=1 if flag_bar_outline else 0.9,
        )
    )
    fig_obj.add_trace(  # bar 2
        go.Bar(
            x=sub_plot_data.x,
            y=sub_plot_data.y2,
            name=sub_plot_data.legends[1],
            marker_color=sub_plot_data.colors[1],
            marker_line_color="black" if flag_bar_outline else sub_plot_data.colors[1],
            marker_line_width=1.5 if flag_bar_outline else 0,
            width=0.35,
            opacity=1 if flag_bar_outline else 0.9,
        )
    )


def get_monthly_plotly_figure_obj(type_str):
    """
    Return thr fig obj according to input type string.
    """
    data = MonthlyFigData()
    if type_str == TISA:
        data.init_data(tisa_by_month_data, TISA)
    elif type_str == AQUA:
        data.init_data(aqua_by_month_data, AQUA)
    elif type_str == TERRA:
        data.init_data(terra_by_month_data, TERRA)

    all_months = list(data.sub_1_data.x) + list(data.sub_2_data.x)  # join the x-axis

    fig = go.Figure()
    add_two_bar_traces(fig, data.sub_1_data, False)     # add the version3c bars
    add_two_bar_traces(fig, data.sub_2_data, True)      # the the version4a bars
    fig.add_trace(go.Scatter(                               # add 90% line
        x=all_months,
        y=[90] * len(all_months),
        name='90% success rate',
        line=dict(color="slategray", dash="dash")
    ))

    fig.update_layout(
        barmode='group',
        title=dict(
            text=data.get_title_str(type_str),
            font_size=20,
        ),
        yaxis=dict(
            title='Success rate (%)',
            titlefont_size=16,
            tickfont_size=14,
            range=[0, 105],
        ),
        xaxis=dict(
            tickangle=-90,  # rotate x labels
            titlefont_size=16,
            tickfont_size=14,
            title='Month',
        ),
        legend=dict(
            title='Latency',
            orientation="h",
            font_size=12,
            x=0,  y=1.1,  # legend position, can adjust
            bgcolor='rgba(255, 255, 255, 0)',  # the same as the background color
            bordercolor='rgba(255, 255, 255, 0)'
        )
    )

    # fig.show()   # for debug
    return fig


def get_annual_plotly_figure_obj():

    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.6, 0.3],
        # horizontal_spacing=0.05,
        # shared_yaxes=True,
        subplot_titles=("FLASHFlux v3C products", "FLASHFlux v4A products")
    )

    x_axis_v3c, x_axis_v4a = aqua_by_year_data.v3c.x, aqua_by_year_data.v4a.x

    # the first subplot
    fig.add_trace(   # Aqua_v3C, delay in 3 days
        go.Bar(
            x=x_axis_v3c,
            y=aqua_by_year_data.v3c.y1,
            name='Aqua ' + VERSION_STR[0] + ': ' + aqua_by_year_data.v3c.y1_legend_str,
            marker_color=AQUA_BAR_COLORS[0]
        ),
        row=1, col=1
    )

    fig.add_trace(   # Aqua_v3C, delay in 4 days
        go.Bar(
            x=x_axis_v3c,
            y=aqua_by_year_data.v3c.y2,
            name='Aqua ' + VERSION_STR[0] + ': ' + aqua_by_year_data.v3c.y2_legend_str,
            marker_color=AQUA_BAR_COLORS[1]
        ),
        row=1, col=1
    )

    fig.add_trace(  # Terra_v3C, delay in 3 days
        go.Bar(
            x=x_axis_v3c,
            y=terra_by_year_data.v3c.y1,
            name='Terra ' + VERSION_STR[0] + ': ' + terra_by_year_data.v3c.y1_legend_str,
            marker_color=TERRA_BAR_COLORS[0]
        ),
        row=1, col=1
    )

    fig.add_trace(  # Terra_v3C, delay in 4 days
        go.Bar(
            x=x_axis_v3c,
            y=terra_by_year_data.v3c.y2,
            name='Terra ' + VERSION_STR[0] + ': ' + terra_by_year_data.v3c.y2_legend_str,
            marker_color=TERRA_BAR_COLORS[1]
        ),
        row=1, col=1
    )

    fig.add_trace(  # TISA_v3C, delay in 6 days
        go.Bar(
            x=x_axis_v3c,
            y=tisa_by_year_data.v3c.y1,
            name='TISA ' + VERSION_STR[0] + ': ' + tisa_by_year_data.v3c.y1_legend_str,
            marker_color=TISA_BAR_COLORS[0]
        ),
        row=1, col=1
    )

    fig.add_trace(  # TISA_v3C, delay in 7 days
        go.Bar(
            x=x_axis_v3c,
            y=tisa_by_year_data.v3c.y2,
            name='TISA ' + VERSION_STR[0] + ': ' + tisa_by_year_data.v3c.y2_legend_str,
            marker_color=TISA_BAR_COLORS[1]
        ),
        row=1, col=1
    )

    fig.update_xaxes(
        titlefont_size=16,
        tickfont_size=14,
        title_text="Year",
        row=1, col=1
    )
    fig.update_yaxes(
        title_text='Success rate (%)',
        titlefont_size=16,
        tickfont_size=14,
        range=[0, 90],
        row=1, col=1
    )

    # the second subplot
    fig.add_trace(   # Aqua_v4A, delay in 3 days
        go.Bar(
            x=x_axis_v4a,
            y=aqua_by_year_data.v4a.y1,
            name='Aqua ' + VERSION_STR[1] + ': ' + aqua_by_year_data.v4a.y1_legend_str,
            marker_color=AQUA_BAR_COLORS[0],
            marker_line_color="black",
            marker_line_width=1.5,
        ),
        row=1, col=2
    )

    fig.add_trace(   # Aqua_v4A, delay in 4 days
        go.Bar(
            x=x_axis_v4a,
            y=aqua_by_year_data.v4a.y2,
            name='Aqua ' + VERSION_STR[1] + ': ' + aqua_by_year_data.v4a.y2_legend_str,
            marker_color=AQUA_BAR_COLORS[1],
            marker_line_color="black",
            marker_line_width=1.5,
        ),
        row=1, col=2
    )

    fig.add_trace(  # Terra_v4A, delay in 3 days
        go.Bar(
            x=x_axis_v4a,
            y=terra_by_year_data.v4a.y1,
            name='Terra ' + VERSION_STR[1] + ': ' + terra_by_year_data.v4a.y1_legend_str,
            marker_color=TERRA_BAR_COLORS[0],
            marker_line_color="black",
            marker_line_width=1.5,
        ),
        row=1, col=2
    )

    fig.add_trace(  # Terra_v4A, delay in 4 days
        go.Bar(
            x=x_axis_v4a,
            y=terra_by_year_data.v4a.y2,
            name='Terra ' + VERSION_STR[1] + ': ' + terra_by_year_data.v4a.y2_legend_str,
            marker_color=TERRA_BAR_COLORS[1],
            marker_line_color="black",
            marker_line_width=1.5,
        ),
        row=1, col=2
    )

    fig.add_trace(  # TISA_v4A, delay in 6 days
        go.Bar(
            x=x_axis_v4a,
            y=tisa_by_year_data.v4a.y1,
            name='TISA ' + VERSION_STR[1] + ': ' + tisa_by_year_data.v4a.y1_legend_str,
            marker_color=TISA_BAR_COLORS[0],
            marker_line_color="black",
            marker_line_width=1.5,
        ),
        row=1, col=2
    )

    fig.add_trace(  # TISA_v4A, delay in 7 days
        go.Bar(
            x=x_axis_v4a,
            y=tisa_by_year_data.v4a.y2,
            name='TISA ' + VERSION_STR[1] + ': ' + tisa_by_year_data.v4a.y2_legend_str,
            marker_color=TISA_BAR_COLORS[1],
            marker_line_color="black",
            marker_line_width=1.5,
        ),
        row=1, col=2
    )

    fig.update_xaxes(
        titlefont_size=16,
        tickfont_size=14,
        title_text="Year",
        row=1, col=2,
    )

    fig.update_yaxes(
        title_text='Success rate (%)',
        titlefont_size=16,
        tickfont_size=14,
        range=[0, 90],
        row=1, col=2,
    )

    # overall layout
    fig.update_layout(
        title=dict(
            text='FLASHFlux Annual Latency Success Rates',
            font_size=20,
        ),
        legend=dict(
            title='Latency',
            font_size=12,
            x=1, y=1,  # legend position, can adjust
            bgcolor='rgba(255, 255, 255, 0)',  # the same as the background color
            bordercolor='rgba(255, 255, 255, 0)'
        )
    )

    # fig.show()
    return fig


def get_latency_figure_obj(type_str):
    if type_str in BY_MONTH_TYPE_STR:
        return get_monthly_plotly_figure_obj(type_str)
    elif type_str == BY_YEAR_STR:
        return get_annual_plotly_figure_obj()


# for debug
# get_monthly_plotly_figure_obj(TISA)
# get_latency_figure_obj(BY_YEAR_STR)
