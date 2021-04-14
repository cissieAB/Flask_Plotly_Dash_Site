"""
This file reads the .csv files from `../data/latency` and prepare them for Plotly
bar chart plots.

It can be debugged independently.
"""
import pandas as pd
from os.path import join

from apps.dashapp_latency.path_constants import PATH_PREFIX
from apps.dashapp_latency.constants import *

FLAG_MONTH_STR = "M"
FLAG_YEAR_STR = "Y"


class SingleFileLatencyData:
    def __init__(self, name_str):
        self.data_name = name_str
        self.x = []     # x axis
        self.y1 = []    # first bar values
        self.y2 = []    # second bar values
        self.y1_legend_str = ""   # first bar legend
        self.y2_legend_str = ""   # second bar legend

    def format_y_values(self, array):
        """
        Round a column of float values (of many digits) to only one digit.
        """
        y = []
        for num in array:
            y.append(round(num, 1))  # round to 1 digit
        return y

    def get_legend_name(self, column_name_str):
        """
        Get the legend name according to the column name string of the dataframe.
        :param column_name_str: with a form of "x_days_SR(%)"
        :return: a string with a form of "Delay in x days"
        """
        return "delay in " + column_name_str[0] + " days"

    def get_plot_data_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        self.x = df.iloc[:, 0].values

        # read the second column
        self.y1_legend_str = self.get_legend_name(df.iloc[:, 1].name)   # column name
        self.y1 = self.format_y_values(df.iloc[:, 1])

        # read the third column
        self.y2_legend_str = self.get_legend_name(df.iloc[:, 2].name)   # column name
        self.y2 = self.format_y_values(df.iloc[:, 2])


class PackedMultiVersionLatencyData:
    def __init__(self, type_str, freq_str):
        # get v3C data
        self.v3c = SingleFileLatencyData(self.get_name_str(type_str, VERSION_STR[0]))
        self.v3c.get_plot_data_from_csv(self.get_path_str(type_str, VERSION_STR[0], freq_str))

        # get v4A data
        self.v4a = SingleFileLatencyData(self.get_name_str(type_str, VERSION_STR[1]))
        self.v4a.get_plot_data_from_csv(self.get_path_str(type_str, VERSION_STR[1], freq_str))

    def get_path_str(self, type_str, version_str, freq_str):
        # should be identical with the file name
        suffix_str = "_SR_by_month.csv" if freq_str == "M" else "_SR_by_year.csv"
        csv_name_str = self.get_name_str(type_str, version_str) + suffix_str
        path_str = join(PATH_PREFIX, csv_name_str)
        # print(path_str)
        return path_str

    def get_name_str(self, type_str, version_str):
        return type_str + "_" + version_str


aqua_by_month_data = PackedMultiVersionLatencyData(AQUA, FLAG_MONTH_STR)
terra_by_month_data = PackedMultiVersionLatencyData(TERRA, FLAG_MONTH_STR)
tisa_by_month_data = PackedMultiVersionLatencyData(TISA, FLAG_MONTH_STR)

aqua_by_year_data = PackedMultiVersionLatencyData(AQUA, FLAG_YEAR_STR)
terra_by_year_data = PackedMultiVersionLatencyData(TERRA, FLAG_YEAR_STR)
tisa_by_year_data = PackedMultiVersionLatencyData(TISA, FLAG_YEAR_STR)

# for debug
# print(aqua_by_year_data.v3c.y1, tisa_by_month_data.v3c.y1)
